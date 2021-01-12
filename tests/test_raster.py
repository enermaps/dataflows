from dataflows import Flow, dump_to_path, load

import os

# Make sure to use the latest PROJ library (here in the rasterflows environment)
os.environ["PROJ_LIB"] = "{}/opt/anaconda3/envs/rasterflows/share/proj/".format(
    os.path.expanduser("~")
)


def test_geotiff():
    """
    Test a geotiff dataflow.
    Sample open dataset from https://www.opendata-hro.de/en/dataset/schmettau_1788
    Originally in EPSG:25833, convert it into EPSG:4326
    """
    Flow(
        load(
            "https://geo.sv.rostock.de/download/opendata/schmettau_1788/schmettau_1788.tiff",
            format="raster",
        ),
        dump_to_path("schmettau_1788", format="geotiff", projection="EPSG:4326"),
    ).process()


def test_netcdf():
    """
    Test a netcdf dataflow.
    """
    Flow(
        load(
            "../data/NEWA-2009-12-30_100m_30min.nc",
            format="NetCDF",
        ),
        dump_to_path("../out/NEWA-2009-12-30_100m_30min", format="geotiff"),
    ).process()


# test_geotiff()
test_netcdf()
# import xarray as xr

# ds  = xr.open_dataset("../data/NEWA-2009-12-30_100m_30min.nc")
# import pandas as pd
# print(ds.variables)
# pd.DataFrame(ds.variables["Times"].values)
# ds.to_array(dim="Times").to_pandas().to_csv("test.csv")
