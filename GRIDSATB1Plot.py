import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
import requests
import os
def download_gridsat_nc(year, month, day, hour):
    
    month = str(month).zfill(2)
    day = str(day).zfill(2)
    hour = str(hour).zfill(2)

    # Construct the URL
    url = f"https://www.ncei.noaa.gov/data/geostationary-ir-channel-brightness-temperature-gridsat-b1/access/{year}/GRIDSAT-B1.{year}.{month}.{day}.{hour}.v02r01.nc"
    
    # Download the file
    response = requests.get(url)
    destination = 'gridsatfile.nc'
    # Check if the request was successful
    if response.status_code == 200:
        # Save the file
        with open(destination, 'wb') as f:
            f.write(response.content)
        print("File downloaded successfully!")
    else:
        print("Failed to download file.")

# Example usage:
year = 1987
month = 9
day = 8
hour = 18

# Define the center latitude and longitude and the extent
center_lat = 20.62 # Center latitude
center_lon = 122.47  # Center longitude
extent = 8  # Extent in degrees

destination = 'gridsatfile.nc'

download_gridsat_nc(year, month, day, hour)

# Load the NetCDF file
dataset = xr.open_dataset(destination, decode_times=False)

# Extract latitude, longitude, and infrared brightness temperature data
lat = dataset['lat']
lon = dataset['lon']
brightness_temp = dataset['irwin_cdr']

# Select a specific time slice (for example, the first time step)
brightness_temp_slice = brightness_temp.isel(time=0)



# Calculate the bounds
lat_min, lat_max = center_lat - extent, center_lat + extent
lon_min, lon_max = center_lon - extent, center_lon + extent


# Select data within the specified bounds
selected_lat = lat[(lat >= lat_min) & (lat <= lat_max)]
selected_lon = lon[(lon >= lon_min) & (lon <= lon_max)]
selected_brightness_temp = brightness_temp_slice.sel(lat=slice(lat_min, lat_max), lon=slice(lon_min, lon_max))

# Select data within the specified bounds
selected_eye_temp = brightness_temp_slice.sel(lat=slice(center_lat-1, center_lat+1), lon=slice(center_lon-1, center_lon+1))

# Find the maximum temperature
max_temp = "{:.2f}".format(np.max(selected_eye_temp.values))

def kelvin_to_celsius(kelvin_temp):
    celsius_temp = float(kelvin_temp) - 273.15
    return "{:.2f}".format(celsius_temp)


# Create a map projection using Cartopy
projection = ccrs.PlateCarree()

# Plot the data on a map using pcolormesh
plt.figure(figsize=(10, 8))  # Set plot size
ax = plt.axes(projection=projection)
pcolor = ax.pcolormesh(selected_lon, selected_lat, selected_brightness_temp, cmap='CMRmap', transform=projection)
ax.coastlines()  # Add coastlines
ax.set_xlabel('Longitude (degrees_east)')
ax.set_ylabel('Latitude (degrees_north)')
ax.set_title(f'GRIDSAT B1 Brightness Temperature IR on {str(hour).zfill(2)}:00 UTC {day}/{month}/{year}\nCentered at ({center_lat}, {center_lon}) +/- 5 degrees, Max eye temp = {kelvin_to_celsius(max_temp)} °C')
gls = ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
gls.top_labels = False   # suppress top labels
gls.right_labels = False  # suppress right labels
cbar = plt.colorbar(pcolor, label='Brightness Temperature (Kelvin)')
plt.show()

dataset.close()
os.remove(destination)
