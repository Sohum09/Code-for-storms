import subprocess, sys, datetime, requests
packages = ["cartopy"]
for package in packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime, timedelta
import glob
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

def mw85():
  newcmp = LinearSegmentedColormap.from_list("", [
    (0/100, '#0507b4'),
    (10/100, "#0457cf"),
    (20/100, "#06a5eb"),
    (26/100, "#0ad5c2"),
    (26/100, "#0bb617"),
    (30/100, "#20bc01"),
    (40/100, "#4fd200"),
    (50/100, "#80ec02"),
    (52/100, "#8ef101"),
    (52/100, "#f1e400"),
    (60/100, "#f2de01"),
    (68/100, "#f8c30d"),
    (68/100, "#f90602"),
    (70/100, "#f40a03"),
    (80/100, "#da280a"),
    (90/100, "#be4411"),
    (100/100, "#a36319"),])

  vmax = 280
  vmin = 180

  return newcmp.reversed(), vmax, vmin

def mw37():
  newcmp = LinearSegmentedColormap.from_list("", [
    (0/115, '#7f0102'),
    (5/115, '#9a1a02'),
    (15/115, "#d05102"),
    (25/115, "#fd8608"),
    (35/115, "#f5c141"),
    (45/115, "#e0c66e"),
    (55/115, "#98f68c"),
    (65/115, "#9fe4c9"),
    (75/115, "#60e0fe"),
    (85/115, "#24a4fe"),
    (95/115, "#106dee"),
    (105/115, "#4c33b3"),
    (115/115, "#7f017e"),])

  vmax = 280
  vmin = 165

  return newcmp.reversed(), vmax, vmin

# Load netCDF data here =
nc_paths = sorted(glob.glob("/content/*.nc")) #No need to touch this anymore, it automatically loads the files once uploaded

#-------------------USER INPUT HERE--------------------------------------------------------------
mw_type = "85" #Change accordingly, accepted values are [85, 37]
cmap, vmax, vmin = mw85() #Change to mw37() if mw_type = "37"
idl_flag = True #If the storm is expected to cross the IDL, set this to True
#------------------------------------------------------------------------------------------------

for nc_path in nc_paths:
  ds = xr.open_dataset(nc_path)
  type_map = {"85": "T85H", "37":"T37H"}
  # Extracting variables from netCDF file
  mw_values = ds[type_map[mw_type]].values  # MW data
  lat = ds["lat"].values
  lon = ds["lon"].values
  bt_lat = ds["CentLat"].values  # Best track latitude
  bt_lon = ds["CentLon"].values  # Best track longitude
  satellite_name = ds.attrs.get("Satellite_Name")  # Satellite name
  arr = nc_path.split('.')
  bt_time = f"{arr[5]} UTC, {arr[4]}/{arr[3]}/{arr[2]}" 
  
  for i in range (len(mw_values)):
    for j in range(len(mw_values[0])):
      if mw_values[i][j] == -1:
        mw_values[i][j] = np.nan

  # Handling NaN values if present
  mw_values = np.ma.masked_invalid(mw_values)

  # Setting up the plot with Cartopy
  fig = plt.figure(figsize=(10, 8))
  if idl_flag:
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
  else:
    ax = plt.axes(projection=ccrs.PlateCarree())
  ax.set_extent([lon[-1], lon[0], lat[-1], lat[0]], crs=ccrs.PlateCarree())

  # Addding map features
  ax.add_feature(cfeature.COASTLINE, linewidth=1, color='magenta')
  ax.add_feature(cfeature.BORDERS, linestyle=':', linewidth=0.5)

  if not idl_flag:
    gls = ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
  else:
    gls = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.5, color='gray', linestyle='--')
    gls.xlocator = mticker.FixedLocator(range(-180, 181, 3))  # Control gridline spacing
    gls.ylocator = mticker.FixedLocator(range(-90, 91, 3))
    #gls.xformatter = LONGITUDE_FORMATTER
    gls.yformatter = LATITUDE_FORMATTER
    gls.xlabel_style = {'size': 8, 'color': 'k'}  # Customize label style
    gls.ylabel_style = {'size': 8, 'color': 'k'}
  gls.top_labels = False
  gls.right_labels = False

  # Plotting the MW data
  temp_plot = ax.pcolormesh(lon, lat, mw_values, cmap=cmap, vmin=vmin, vmax=vmax, transform=ccrs.PlateCarree())

  # Adding the colorbar
  cbar = plt.colorbar(temp_plot, ax=ax, orientation="vertical", shrink=0.7, pad=0.05)
  cbar.set_label("MW Temperature (°C)")

  # Set custom ticks in Celsius with intervals of 10°C
  celsius_tick_values = np.arange(-95, 20, 10)  # Adjusting the range if needed
  kelvin_tick_values = celsius_tick_values + 273.15  # Convert Celsius ticks to Kelvin

  # Update the colorbar ticks and labels
  cbar.set_ticks(kelvin_tick_values)  # Set the ticks in Kelvin
  cbar.set_ticklabels([f"{int(temp)}°C" for temp in celsius_tick_values])  # Label them in Celsius

  plt.title(
      f"MW {type_map[mw_type]} Brightness Temperature MW"+
      f" At {bt_time}\n"+
      f"Name: {arr[1]}, Satellite: {satellite_name}"
  )

  # Display
  plt.show()
