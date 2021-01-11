# WIP Raster support

Development of a frictionless-based pipeline for raster geodata using:

- datapackage-py

- dataflows

- gdal

## Installation

- Create a new `rasterflows` environment
```conda create --name rasterflows python=3.7.3```

- Activate the environment and install gdal
```
conda activate rasterflows
conda install gdal -y
```

- Clone and install datapackage-py (raster branch)
```
git clone git@github.com:enermaps/datapackage-py.git
cd datapackage-py
git checkout raster
pip install -e .
```

- Clone and install dataflows (raster branch)
```
git clone git@github.com:enermaps/dataflows.git
cd dataflows
git checkout raster
pip install -e .
```

## Use
Within the ```rasterflows``` environment run:

```python tests/test_raster.py```

This is a sample test of reprojection of a GeoTIFF file from an online repository.


## TODO

- Support for NetCDF and other formats (as input)

- Support for raster data contained in zipped archives

- Support for multiband files

- Define projection requirements (for input files)

- Define schema for raster (based on Hotmaps early example)

