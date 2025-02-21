import datetime as dt
import glob
import logging
import os
import re

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import dask.array as da
import imageio_ffmpeg as ffmpeg
import matplotlib as mpl
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rioxarray
import xarray as xr

from cartopy.feature import ShapelyFeature, NaturalEarthFeature
from cartopy.feature import AdaptiveScaler
from functools import cache
from ibicus.debias import LinearScaling
from matplotlib.path import Path
from pyproj import CRS, Transformer
from rasterio.enums import Resampling
from shapely.geometry import Polygon

from icenet.data.sic.mask import Masks

def broadcast_forecast(start_date: object,
                       end_date: object,
                       datafiles: object = None,
                       dataset: object = None,
                       target: object = None) -> object:
    """

    :param start_date:
    :param end_date:
    :param datafiles:
    :param dataset:
    :param target:
    :return:
    """

    assert (datafiles is None) ^ (dataset is None), \
        "Only one of datafiles and dataset can be set"

    if datafiles:
        logging.info("Using {} to generate forecast through {} to {}".format(
            ", ".join(datafiles), start_date, end_date))
        dataset = xr.open_mfdataset(datafiles, engine="netcdf4")

    dates = pd.date_range(start_date, end_date)
    i = 0

    logging.debug("Dataset summary: \n{}".format(dataset))

    if len(dataset.time.values) > 1:
        while dataset.time.values[i + 1] < dates[0]:
            i += 1

    logging.info("Starting index will be {} for {} - {}".format(
        i, dates[0], dates[-1]))
    dt_arr = []

    for d in dates:
        logging.debug("Looking for date {}".format(d))
        arr = None

        while arr is None:
            if d >= dataset.time.values[i]:
                d_lead = (d - dataset.time.values[i]).days

                if i + 1 < len(dataset.time.values):
                    if pd.to_datetime(dataset.time.values[i]) + \
                            dt.timedelta(days=d_lead) >= \
                            pd.to_datetime(dataset.time.values[i + 1]) + \
                            dt.timedelta(days=1):
                        i += 1
                        continue

                logging.debug("Selecting date {} and lead {}".format(
                    pd.to_datetime(dataset.time.values[i]).strftime("%D"),
                    d_lead))

                arr = dataset.sel(time=dataset.time.values[i],
                                  leadtime=d_lead).\
                    copy().\
                    drop("time").\
                    assign_coords(dict(time=d)).\
                    drop("leadtime")
            else:
                i += 1

        dt_arr.append(arr)

    target_ds = xr.concat(dt_arr, dim="time")

    if target:
        logging.info("Saving dataset to {}".format(target))
        target_ds.to_netcdf(target)
    return target_ds


def get_seas_forecast_init_dates(
    hemisphere: str,
    source_path: object = os.path.join(".", "data", "mars.seas")
) -> object:
    """
    Obtains list of dates for which we have SEAS forecasts we have.

    :param hemisphere: string, typically either 'north' or 'south'
    :param source_path: path where north and south SEAS forecasts are stored

    :return: list of dates
    """
    # list the files in the path where SEAS forecasts are stored
    filenames = os.listdir(os.path.join(source_path, hemisphere, "siconca"))
    # obtain the dates from files with YYYYMMDD.nc format
    return pd.to_datetime(
        [x.split('.')[0] for x in filenames if re.search(r'^\d{8}\.nc$', x)])


def get_seas_forecast_da(
        hemisphere: str,
        date: str,
        bias_correct: bool = True,
        source_path: object = os.path.join(".", "data", "mars.seas"),
) -> tuple:
    """
    Atmospheric model Ensemble 15-day forecast (Set III - ENS)

Coordinates:
  * time                          (time) datetime64[ns] 2022-04-01 ... 2022-0...
  * yc                            (yc) float64 5.388e+06 ... -5.388e+06
  * xc                            (xc) float64 -5.388e+06 ... 5.388e+06

    :param hemisphere: string, typically either 'north' or 'south'
    :param date:
    :param bias_correct:
    :param source_path:
    """

    seas_file = os.path.join(
        source_path, hemisphere, "siconca",
        "{}.nc".format(date.replace(day=1).strftime("%Y%m%d")))

    if os.path.exists(seas_file):
        seas_da = xr.open_dataset(seas_file).siconc
    else:
        logging.warning("No SEAS data available at {}".format(seas_file))
        return None

    if bias_correct:
        # Let's have some maximum, though it's quite high
        (start_date, end_date) = (date - dt.timedelta(days=10 * 365),
                                  date + dt.timedelta(days=10 * 365))
        obs_da = get_obs_da(hemisphere, start_date, end_date)
        seas_hist_files = dict(
            sorted({
                os.path.abspath(el):
                    dt.datetime.strptime(os.path.basename(el)[0:8], "%Y%m%d")
                for el in glob.glob(
                    os.path.join(source_path, hemisphere, "siconca", "*.nc"))
                if re.search(r'^\d{8}\.nc$', os.path.basename(el)) and
                el != seas_file
            }.items()))

        def strip_overlapping_time(ds):
            data_file = os.path.abspath(ds.encoding["source"])

            try:
                idx = list(seas_hist_files.keys()).index(data_file)
            except ValueError:
                logging.exception("\n{} not in \n\n{}".format(
                    data_file, seas_hist_files))
                return None

            if idx < len(seas_hist_files) - 1:
                max_date = seas_hist_files[
                               list(seas_hist_files.keys())[idx + 1]] \
                           - dt.timedelta(days=1)
                logging.debug("Stripping {} to {}".format(data_file, max_date))
                return ds.sel(time=slice(None, max_date))
            else:
                logging.debug("Not stripping {}".format(data_file))
                return ds

        hist_da = xr.open_mfdataset(seas_hist_files,
                                    preprocess=strip_overlapping_time).siconc
        debiaser = LinearScaling(delta_type="additive",
                                 variable="siconc",
                                 reasonable_physical_range=[0., 1.])

        logging.info("Debiaser input ranges: obs {:.2f} - {:.2f}, "
                     "hist {:.2f} - {:.2f}, fut {:.2f} - {:.2f}".format(
                         float(obs_da.min()), float(obs_da.max()),
                         float(hist_da.min()), float(hist_da.max()),
                         float(seas_da.min()), float(seas_da.max())))

        seas_array = debiaser.apply(obs_da.values, hist_da.values,
                                    seas_da.values)
        seas_da.values = seas_array
        logging.info("Debiaser output range: {:.2f} - {:.2f}".format(
            float(seas_da.min()), float(seas_da.max())))

    logging.info("Returning SEAS data from {} from {}".format(seas_file, date))

    # This isn't great looking, but we know we're not dealing with huge
    # indexes in here
    date_location = list(seas_da.time.values).index(pd.Timestamp(date))
    if date_location > 0:
        logging.warning("SEAS forecast started {} day before the requested "
                        "date {}, make sure you account for this!".format(
                            date_location, date))

    seas_da = seas_da.sel(time=slice(date, None))
    logging.debug("SEAS data range: {} - {}, {} dates".format(
        pd.to_datetime(min(seas_da.time.values)).strftime("%Y-%m-%d"),
        pd.to_datetime(max(seas_da.time.values)).strftime("%Y-%m-%d"),
        len(seas_da.time)))

    return seas_da


def get_forecast_ds(forecast_file: object,
                    forecast_date: str,
                    stddev: bool = False) -> object:
    """

    :param forecast_file: a path to a .nc file
    :param forecast_date: initialisation date of the forecast
    :param stddev:
    :returns tuple(fc_ds, obs_ds, land_mask):
    """
    forecast_date = pd.to_datetime(forecast_date)

    forecast_ds = xr.open_dataset(forecast_file, decode_coords="all")
    get_key = "sic_mean" if not stddev else "sic_stddev"

    forecast_ds = getattr(
        forecast_ds.sel(time=slice(forecast_date, forecast_date)), get_key)

    return forecast_ds


def filter_ds_by_obs(ds: object, obs_da: object, forecast_date: str) -> object:
    """

    :param ds:
    :param obs_da:
    :param forecast_date: initialisation date of the forecast
    :return:
    """
    forecast_date = pd.to_datetime(forecast_date)
    (start_date,
     end_date) = (forecast_date + dt.timedelta(days=int(ds.leadtime.min())),
                  forecast_date + dt.timedelta(days=int(ds.leadtime.max())))

    if len(obs_da.time) < len(ds.leadtime):
        if len(obs_da.time) < 1:
            raise RuntimeError("No observational data available between {} "
                               "and {}".format(start_date.strftime("%D"),
                                               end_date.strftime("%D")))

        logging.warning("Observational data not available for full range of "
                        "forecast lead times: {}-{} vs {}-{}".format(
                            obs_da.time.to_series()[0].strftime("%D"),
                            obs_da.time.to_series()[-1].strftime("%D"),
                            start_date.strftime("%D"), end_date.strftime("%D")))
        (start_date, end_date) = (obs_da.time.to_series()[0],
                                  obs_da.time.to_series()[-1])

    # We broadcast to get a nicely compatible dataset for plotting
    return broadcast_forecast(start_date=start_date,
                              end_date=end_date,
                              dataset=ds)


def get_obs_da(
        hemisphere: str,
        start_date: str,
        end_date: str,
        obs_source: object = os.path.join(".", "data", "osisaf"),
) -> object:
    """

    :param hemisphere: string, typically either 'north' or 'south'
    :param start_date:
    :param end_date:
    :param obs_source:
    :return:
    """
    obs_years = pd.Series(pd.date_range(start_date, end_date)).dt.year.unique()
    obs_dfs = [
        el for yr in obs_years for el in glob.glob(
            os.path.join(obs_source, hemisphere, "siconca", "{}.nc".format(yr)))
    ]

    if len(obs_dfs) < len(obs_years):
        logging.warning(
            "Cannot find all obs source files for {} - {} in {}".format(
                start_date, end_date, obs_source))

    logging.info("Got files: {}".format(obs_dfs))
    obs_ds = xr.open_mfdataset(obs_dfs)
    obs_ds = obs_ds.sel(time=slice(start_date, end_date))

    return obs_ds.ice_conc


def get_crs(crs_str: str):
    """Get Coordinate Reference System (CRS) from string input argument

    Args:
        crs_str: A CRS given as EPSG code (e.g. `EPSG:3347` for North Canada)
            or, a pre-defined Cartopy CRS call (e.g. "PlateCarree")
    """
    if crs_str.casefold().startswith("epsg"):
        crs = ccrs.epsg(int(crs_str.split(":")[1]))
    elif crs_str == "Mercator.GOOGLE":
        crs = ccrs.Mercator.GOOGLE
    else:
        try:
            crs = getattr(ccrs, crs_str)()
        except AttributeError:
            get_crs_options = [crs_option for crs_option in dir(ccrs)
                                if isinstance(getattr(ccrs, crs_option), type)
                                 and issubclass(getattr(ccrs, crs_option), ccrs.CRS)
                                 ] + ["Mercator.GOOGLE"]
            get_crs_options.sort()
            get_crs_options = ", ".join(get_crs_options)
            raise AttributeError("Unsupported CRS defined, supported options are:",\
                f"{get_crs_options}"
            )

    return crs


def calculate_extents(x1: int, x2: int, y1: int, y2: int):
    """

    :param x1:
    :param x2:
    :param y1:
    :param y2:
    :return:
    """
    data_extent_base = 5387500

    extents = [
        -data_extent_base + (x1 * 25000),
        data_extent_base - ((432 - x2) * 25000),
        -data_extent_base + (y1 * 25000),
        data_extent_base - ((432 - y2) * 25000),
    ]

    logging.debug("Data extents: {}".format(extents))
    return extents


def pixel_to_projection(pixel_x_min, pixel_x_max,
                        pixel_y_min, pixel_y_max,
                        x_min_proj: float=-5387500, x_max_proj: float=5387500,
                        y_min_proj: float=-5387500, y_max_proj: float=5387500,
                        image_width: int=432, image_height: int=432,
                        ):
    """Converts pixel coordinates to CRS projection coordinates"""
    proj_x_min = (pixel_x_min / image_width ) * (x_max_proj - x_min_proj) + x_min_proj
    proj_x_max = (pixel_x_max / image_width ) * (x_max_proj - x_min_proj) + x_min_proj
    proj_y_min = (pixel_y_min / image_height) * (y_max_proj - y_min_proj) + y_min_proj
    proj_y_max = (pixel_y_max / image_height) * (y_max_proj - y_min_proj) + y_min_proj

    return proj_x_min, proj_x_max, proj_y_min, proj_y_max


def get_bounds(proj=None, pole=1):
    """Get min/max bounds for a given CRS projection"""
    if proj is None or isinstance(proj, ccrs.LambertAzimuthalEqualArea):
        proj = ccrs.LambertAzimuthalEqualArea(0, pole * 90)
        x_min_proj, x_max_proj = [-5387500, 5387500]
        y_min_proj, y_max_proj = [-5387500, 5387500]
    else:
        x_min_proj, x_max_proj = proj.x_limits
        y_min_proj, y_max_proj = proj.y_limits
    logging.debug(f"Projection bounds: {proj.x_limits}, {proj.y_limits}")
    return proj, x_min_proj, x_max_proj, y_min_proj, y_max_proj


def get_plot_axes(x1: int = 0,
                  x2: int = 432,
                  y1: int = 0,
                  y2: int = 432,
                  north: bool = True,
                  south: bool = False,
                  geoaxes: bool = True,
                  target_crs: object = None,
                  figsize: int = (10, 8),
                  dpi: int = 150,
                  ):
    """

    :param x1:
    :param x2:
    :param y1:
    :param y2:
    :param geoaxes:
    :return:
    """
    assert north ^ south, "Only one hemisphere must be selected"

    fig = plt.figure(figsize=figsize, dpi=dpi, layout="tight")

    if geoaxes:
        # pole = 1 if north else -1
        # target_crs, x_min_proj, x_max_proj, y_min_proj, y_max_proj = get_bounds(target_crs, pole)
        pole = 1 if north else -1
        proj = ccrs.LambertAzimuthalEqualArea(central_longitude=0, central_latitude=pole*90) if target_crs is None else target_crs

        ax = fig.add_subplot(1, 1, 1, projection=proj)
    else:
        ax = fig.add_subplot(1, 1, 1)

    return fig, ax


def set_plot_geoaxes(ax,
                  region_definition: str = None,
                  extent: list = None,
                  coastlines: str = None,
                  gridlines: bool = False,
                  north: bool = True,
                  south: bool = False,
                  ):
    plt.tight_layout(pad=4.0)

    # Set colour for areas outside of `process_region()` - i.e., no data here.
    ax.set_facecolor("dimgrey")

    pole = 1 if north else -1
    proj = ccrs.LambertAzimuthalEqualArea(0, pole * 90)

    if extent:
        if region_definition == "pixel":
            extents = calculate_extents(*extent)
            ax.set_extent(extents, crs=proj)
        elif region_definition == "geographic":
            lon_min, lon_max, lat_min, lat_max = extent
            # With some projections like Mercator, it doesn't like having exact boundary longitude
            if lon_min == -180:
                lon_min = -179.99
            elif lon_max == 180:
                lon_max = 179.99
            ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())
            clipping_polygon = Polygon(get_geoextent_polygon(extent))
            path = Path(np.array(clipping_polygon.exterior.coords))

    if coastlines:
        auto_scaler = AdaptiveScaler("110m", (("50m", 150), ("10m", 50)))
        land = NaturalEarthFeature("physical", "land", scale="10m", facecolor="dimgrey")
        if extent and region_definition == "geographic":
            clipped_land = ShapelyFeature([clipping_polygon.intersection(geom)
                                           for geom in land.geometries()],
                                           ccrs.PlateCarree(), facecolor="dimgrey")
            ax.add_feature(clipped_land)
            # Draw coastlines explicitly within the clipping region
            ax.add_geometries([clipping_polygon], ccrs.PlateCarree(), edgecolor="red", facecolor="none", linewidth=0.75, linestyle="dashed", zorder=100)
        else:
            ax.add_feature(land)

        # Add OSMnx GeoDataFrame of coastlines
        #gdf = ox.features_from_place("Antarctica", tags={"natural": "coastline"})
        #gdf.plot(ax=ax, facecolor='none', edgecolor='black', linewidth=0.5)
        ax.coastlines(resolution=auto_scaler)

    if gridlines:
        gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True)

        # Prevent generating labels beneath the colourbar
        gl.top_labels = False
        gl.right_labels = False

    return ax

def get_geoextent_polygon(extent, crs=ccrs.PlateCarree(), n_points=100):
    """Create a high-resolution polygon for the boundary.

    Increase the number of points to approximate the curved edges
    Define the number of interpolation points for the curves
    """
    lon_min, lon_max, lat_min, lat_max = extent

    # Create arrays for the curved sections
    lon_values_bottom = np.linspace(lon_min, lon_max, n_points)
    lat_values_left = np.linspace(lat_min, lat_max, n_points)

    # Create a polygon by defining more points along the edges
    polygon = []

    # Bottom edge (lat_min)
    for lon in lon_values_bottom:
        polygon.append([lon, lat_min])

    # Right edge (lon_max)
    for lat in lat_values_left:
        polygon.append([lon_max, lat])

    # Top edge (lat_max)
    for lon in lon_values_bottom[::-1]:
        polygon.append([lon, lat_max])

    # Left edge (lon_min)
    for lat in lat_values_left[::-1]:
        polygon.append([lon_min, lat])

    return polygon

def set_plot_geoextent(ax, extent, crs=ccrs.PlateCarree(), n_points=100):
    """Create a high-resolution polygon for the boundary
    """
    ax.set_extent(extent, crs=crs)

    # Create polygon and convert it to a matplotlib Path
    polygon = Path(get_geoextent_polygon(extent), crs=crs, n_points=n_points)

    # Show polygon patch in plot
    patch = patches.PathPatch(polygon, facecolor='orange', lw=2, transform=ccrs.PlateCarree())
    #ax.add_patch(patch)

    # Sets custom boundary, buggy with small lat/lon bounds
    # Coastlines, land, and gridlines spill outside of boundary
    ax.set_boundary(polygon, transform=ccrs.PlateCarree())


def show_img(ax,
             arr,
             x1: int = 0,
             x2: int = 432,
             y1: int = 0,
             y2: int = 432,
             cmap: object = None,
             geoaxes: bool = True,
             vmin: float = 0.,
             vmax: float = 1.,
             north: bool = True,
             south: bool = False,
             crs: object = None,
             extents: list = None
             ):
    """

    :param ax:
    :param arr:
    :param x1:
    :param x2:
    :param y1:
    :param y2:
    :param cmap:
    :param geoaxes:
    :param vmin:
    :param vmax:
    :param north:
    :param south:
    :return:
    """

    assert north ^ south, "One hemisphere only must be selected"

    if geoaxes:
        pole = 1 if north else -1
        data_crs = ccrs.LambertAzimuthalEqualArea(0, pole * 90)
        extents = calculate_extents(x1, x2, y1, y2)
        im = ax.imshow(arr,
                       vmin=vmin,
                       vmax=vmax,
                       cmap=cmap,
                       transform=data_crs,
                       extent=extents)
        ax.coastlines()
    else:
        im = ax.imshow(arr, cmap=cmap, vmin=vmin, vmax=vmax)

    return im


def process_probes(probes, data) -> tuple:
    """
    :param probes: A sequence of locations (pairs)
    :param data: A sequence of xr.DataArray
    """

    # index into each element of data with a xr.DataArray, for pointwise
    # selection.  Construct the indexing DataArray as follows:

    probes_da = xr.DataArray(probes, dims=('probe', 'coord'))
    xcs, ycs = probes_da.sel(coord=0), probes_da.sel(coord=1)

    for idx, arr in enumerate(data):
        arr = arr.assign_coords({
            "xi": ("xc", np.arange(len(arr.xc))),
            "yi": ("yc", np.arange(len(arr.yc))),
        })
        if arr is not None:
            data[idx] = arr.isel(xc=xcs, yc=ycs)

    return data


def reproject_array(array, target_crs):
    return array.rio.reproject(target_crs.proj4_init,
        # resampling=Resampling.bilinear,
        nodata=np.nan
        )

def process_block(block, target_crs):
    # dataarray = xr.DataArray(block, dims=["leadtime", "y", "x"])
    dataarray = block
    reprojected = reproject_array(dataarray, target_crs)
    return reprojected.drop_vars(["time"])


def reproject_projected_coords(data: object,
                                target_crs: object,
                                pole: int=1,
                                ) -> object:
    """
    Reprojects an xarray Dataset from LambertAzimuthalEqualArea to `target_crs`.

    The Dataset is expected to have dims of (xc, yc).

    Args:
        data: xarray dataset with dims (xc, yc), and also coords of lon and lat.
        target_crs: Cartopy CRS to project to (e.g. `ccrs.Mercator()`)
        pole: Whether north (`1`) or south pole (`-1`).

    Returns:
        Reprojected data as an xarray dataset.

    Examples:

    >>> reprojected_data = reproject_projected_coords(arr, # doctest: +SKIP
    >>>             target_crs=target_crs,
    >>>             pole=pole,
    >>>             )
    """
    # Eastings/Northings projection
    data_crs_proj = ccrs.LambertAzimuthalEqualArea(0, pole*90)
    # geographic projection
    data_crs_geo = ccrs.PlateCarree()

    data_reproject = data.copy()
    data_reproject = data_reproject.assign_coords({"xc": data_reproject.xc.data*1000,
                                                   "yc": data_reproject.yc.data*1000
                                                })

    # Need to use correctly scaled xc and yc to get coastlines working even if not reprojecting.
    # So, just return scaled DataArray back and not reproject if don't need to.
    if target_crs == data_crs_proj:
        return data_reproject

    data_reproject = data_reproject.drop_vars(["Lambert_Azimuthal_Grid", "lon", "lat"])

    # Set xc, yc (eastings and northings) projection details
    data_reproject = data_reproject.rename({"xc": "x", "yc": "y"})
    data_reproject.rio.write_crs(data_crs_proj.proj4_init, inplace=True)
    data_reproject.rio.write_nodata(np.nan, inplace=True)

    times = len(data_reproject.time)
    leadtimes = len(data_reproject.leadtime)

    # Create a sample image block for use as template for Dask
    sample_block = data_reproject.isel(time=0, leadtime=0)
    sample_reprojected =  reproject_array(sample_block, target_crs)

    # Create a template DataArray based on the reprojected sample block
    template_shape = (data_reproject.sizes['leadtime'], sample_reprojected.sizes['y'], sample_reprojected.sizes['x'])
    template_data = da.zeros(template_shape, chunks=(1, -1, -1))
    template = xr.DataArray(template_data, dims=['leadtime', 'y', 'x'],
                            coords={'leadtime': data_reproject.coords['leadtime'],
                            'y': sample_reprojected.coords['y'],
                            'x': sample_reprojected.coords['x'],
                            }
                            )

    reprojected_data = []
    for time in range(times):
        leadtime_data = xr.map_blocks(process_block, data_reproject.isel(time=time), template=template, kwargs={"target_crs": target_crs})
        reprojected_data.append(leadtime_data)

    # TODO: Add projection info into DataArray, like the `Lambert_Azimuthal_Grid` dropped above
    reprojected_data = xr.concat(reprojected_data, dim="time")
    reprojected_data.coords["time"] = data_reproject.time.data

    # Set attributes
    reprojected_data.rio.write_crs(target_crs.proj4_init, inplace=True)
    reprojected_data.rio.write_nodata(np.nan, inplace=True)

    # Compute geographic for reprojected image
    transformer = Transformer.from_crs(target_crs.proj4_init, data_crs_geo.proj4_init)
    x = reprojected_data.x.values
    y = reprojected_data.y.values

    X, Y = np.meshgrid(x, y)
    lon_grid, lat_grid = transformer.transform(X, Y)

    reprojected_data["lon"] = (("y", "x"), lon_grid)
    reprojected_data["lat"] = (("y", "x"), lat_grid)

    # Rename back to 'xc' and 'yc', although, these are now in metres rather than 1000 metres
    reprojected_data = reprojected_data.rename({"x": "xc", "y": "yc"})

    return reprojected_data


def projection_to_geographic_coords(data, target_crs):
    # Compute geographic for reprojected image
    transform_crs=ccrs.PlateCarree()
    transformer = Transformer.from_crs(target_crs.proj4_init, transform_crs.proj4_init)
    x = data.xc.values*1000
    y = data.yc.values*1000

    X, Y = np.meshgrid(x, y)
    lon_grid, lat_grid = transformer.transform(X, Y)

    data["lon"] = (("yc", "xc"), lon_grid)
    data["lat"] = (("yc", "xc"), lat_grid)

    return data


def process_region(region: tuple=None,
        data: tuple=None,
        pole: int=1,
        src_da: object=None,
        region_definition: str = "pixel",
    ) -> tuple:
    """Extract subset of pan-Arctic/Antarctic region based on region bounds.

    :param region: Either image pixel bounds, or geographic bounds.
    :param data: Contains list of xarray DataArrays.
    :param region_definition: Whether providing pixel coordinates or geographic (i.e. lon/lat).

    :return:
    """

    if region is not None:
        assert len(region) == 4, "Region needs to be a list of four integers"
        x1, y1, x2, y2 = region
        assert x2 > x1 and y2 > y1, "Region is not valid"
        if region_definition == "geographic":
            assert x1 >= -180 and x2 <= 180, "Expect longitude range to be `-180<=longitude>=180`"

    for idx, arr in enumerate(data):
        if arr is not None and region is not None:
            logging.debug(f"Clipping data to specified bounds: {region}")
            # Case when not an array, but an IceNet Masks class
            if isinstance(arr, Masks):
                if region_definition.casefold() == "geographic":
                    masks = arr
                    xc, yc = src_da.xc, src_da.yc
                    lon, lat = src_da.lon, src_da.lat
                    # Edge cases, where the time dimension is passed in,
                    # seems to be with "./data/osisaf/north/siconca/2020.nc"
                    # and, possibly newer.
                    if "time" in lon.dims:
                        lon = lon.isel(time=0)
                    if "time" in lat.dims:
                        lat = lat.isel(time=0)
                    masks.set_region_by_lonlat(xc, yc, lon,lat, region)
                    data[idx] = masks
                elif region_definition.casefold() == "pixel":
                    data[idx] = arr[..., (432 - y2):(432 - y1), x1:x2]
            else:
                # If array only contains "xc" and "yc", but not "lon" and "lat".
                # Reproject using pyproj to get it.
                if "lon" not in arr.coords and "lat" not in arr.coords:
                    target_crs = ccrs.LambertAzimuthalEqualArea(0, pole*90)
                    arr = projection_to_geographic_coords(arr, target_crs)

                lon, lat = arr.lon, arr.lat

                if region_definition.casefold() == "geographic":
                    # Limit to lon/lat region, within a given tolerance
                    tolerance = 0
                    # Create mask where data is within geographic (lon/lat) region
                    mask = (lon >= x1-tolerance) & (lon <= x2+tolerance) & \
                           (lat >= y1-tolerance) & (lat <= y2+tolerance)

                    # Extract subset within region using where()
                    data[idx] = arr.where(mask.compute(), drop=True)
                elif region_definition.casefold() == "pixel":
                    x_max, y_max = arr.xc.shape[0], arr.yc.shape[0]

                    # Clip the data array to specified pixel region
                    data[idx] = arr[..., (y_max - y2):(y_max - y1), x1:x2]
                else:
                    raise NotImplementedError("Only region_definition='pixel' or 'geographic' bounds are supported")

    return data


@cache
def geographic_box(lon_bounds: np.array, lat_bounds: np.array, segments: int=1):
    """Rectangular boundary coordinates in lon/lat coordinates.

    Args:
        lon_bounds: (min, max) lon values
        lat_bounds: (min, max) lat values
        segments: Number of segments per edge

    Returns:
        (lats, lons) for rectangular boundary region
    """

    segments += 1
    rectangular_sides = 4

    lons = np.empty((segments*rectangular_sides))
    lats = np.empty((segments*rectangular_sides))

    bounds = [
        [0, 0],
        [-1, 0],
        [-1, -1],
        [0, -1],
    ]

    for i, (lat_min, lat_max) in enumerate(bounds):
        lats[i*segments:(i+1)*segments] = np.linspace(lat_bounds[lat_min], lat_bounds[lat_max], num=segments)

    bounds.reverse()

    for i, (lon_min, lon_max) in enumerate(bounds):
        lons[i*segments:(i+1)*segments] = np.linspace(lon_bounds[lon_min], lon_bounds[lon_max], num=segments)

    return lons, lats

def get_custom_cmap(cmap):
    """Creates a new colormap, but with nan set to <0.

    Hack since cartopy needs transparency for nan regions to wraparound
        correctly with pcolormesh.
    """
    colors = cmap(np.linspace(0, 1, cmap.N))
    custom_cmap = mpl.colors.ListedColormap(colors)
    custom_cmap.set_bad("dimgrey", alpha=0)
    custom_cmap.set_under("dimgrey")
    return custom_cmap

def set_ffmpeg_path():
    """Set Matplotlib's ffmpeg exe path to the one from imageio_ffmpeg"""
    ffmpeg_path = ffmpeg.get_ffmpeg_exe()
    plt.rcParams['animation.ffmpeg_path'] = ffmpeg_path
