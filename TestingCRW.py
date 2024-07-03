import netCDF4 as nc
import numpy as np

f = nc.Dataset('ct5km_ssta_v3.1_20240302.nc')
print(f)