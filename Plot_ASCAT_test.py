import datetime
from eumdac.token import AccessToken
from eumdac.datastore import DataStore
import shutil
import zipfile
import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf
import numpy as np
import matplotlib.colors as mcolors
import glob

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'

credentials = (consumer_key, consumer_secret)
token = AccessToken(credentials)
datastore = DataStore(token)

selected_collection = datastore.get_collection('EO:EUM:DAT:METOP:OAS025')

# Set sensing start and end time
end = datetime.datetime(2025, 8, 20, 6, 0)
start = end - datetime.timedelta(hours=6)

selected_products = selected_collection.search(dtstart = start, dtend = end)

print(f'Found Datasets: {selected_products.total_results} datasets for the given time range')
for product in selected_products:
    print(str(product))

#Download the selected products
satellite_search = 'metopb'.lower() # You can change this to 'metopc' or remove the filtering if needed

for product in selected_products:
    product_name = str(product)  # Convert the product object to a string to get the filename
    # Filter by satellite type
    if satellite_search in product_name:
        print(f"Downloading: {product_name}")
        try:
            with product.open() as fsrc, \
                open(fsrc.name, mode='wb') as fdst:
                shutil.copyfileobj(fsrc, fdst)
            print(f"Downloaded {fdst.name}")
        except Exception as e:
            print(f"Failed to download {product}: {e}") # Print the product object for better context on error
    else:
        print(f"Skipping {product_name} as it is not a {satellite_search.upper()} product.")

print("Download process complete.")

#Extract the downloaded zip files
# Get a list of all files in the current directory
all_files = os.listdir('.')

# Filter for zip files
zip_files = [f for f in all_files if f.endswith('.zip')]

print(f"Found {len(zip_files)} zip files to extract.")

for zip_file in zip_files:
    print(f"Extracting: {zip_file}")
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall('.') # Extract to the current directory
        print(f"Successfully extracted: {zip_file}")
    except zipfile.BadZipFile:
        print(f"Error: {zip_file} is not a valid zip file.")
    except Exception as e:
        print(f"Error extracting {zip_file}: {e}")

print("Extraction process complete.")

# Step 5: Open NetCDF files using xarray
import xarray as xr
import os

# Get a list of all files in the current directory
all_files = os.listdir('.nc')

# Filter for NetCDF files that start with 'ascat_' and end with '.nc'
netcdf_files = [f for f in all_files if f.startswith('ascat_') and f.endswith('.nc')]

print(f"Found {len(netcdf_files)} NetCDF files to open.")

# Dictionary to store opened datasets
datasets = {}

for nc_file in netcdf_files:
    print(f"Opening: {nc_file}")
    try:
        ds = xr.open_dataset(nc_file)
        datasets[nc_file] = ds
        print(f"Successfully opened: {nc_file}")
    except Exception as e:
        print(f"Error opening {nc_file}: {e}")

print("All specified NetCDF files have been processed.")

center_lat, center_lon = 28, -73

min_lat = center_lat-5
max_lat = center_lat+5
min_lon = center_lon-5
max_lon = center_lon+5

# Calculate the center latitude and longitude for the plot
plot_center_lat = (min_lat + max_lat) / 2
plot_center_lon = (min_lon + max_lon) / 2

print(f"Plot Center Latitude: {plot_center_lat}")
print(f"Plot Center Longitude: {plot_center_lon}")

import numpy as np

# Initialize variables to store the minimum distance and nearest pixel information
min_distance = float('inf')
nearest_pixel_info = None

for filename, ds in datasets.items():
    try:
        lat_values = ds['lat'].values
        lon_values = ds['lon'].values
        for row_index in range(lat_values.shape[0]):
            for col_index in range(lat_values.shape[1]):
                pixel_lat = lat_values[row_index, col_index]
                pixel_lon = lon_values[row_index, col_index]
                distance = np.sqrt((pixel_lat - plot_center_lat)**2 + (pixel_lon - plot_center_lon)**2)
                if distance < min_distance:
                    min_distance = distance
                    nearest_pixel_info = (filename, (row_index, col_index))

    except KeyError as e:
        print(f"Error: Variable {e} not found in dataset {filename}")
    except Exception as e:
        print(f"Error processing dataset {filename}: {e}")

if nearest_pixel_info:
    print(f"The nearest pixel to the plot center is in file: {nearest_pixel_info[0]} at index: {nearest_pixel_info[1]}")
    print(f"Minimum distance: {min_distance}")
else:
    print("No nearest pixel found. There might be an issue with the datasets or variables.")

# Access the dataset using the filename from nearest_pixel_info
nearest_dataset_name = nearest_pixel_info[0]
nearest_ds = datasets[nearest_dataset_name]

# Extract the 'time' variable from the selected dataset
nearest_pixel_time = nearest_ds['time'].values

print(f"Time at the nearest pixel: {nearest_pixel_time}")

# Extract the index of the nearest pixel
row_index, col_index = nearest_pixel_info[1]

# Extract the single time value at the nearest pixel's index
nearest_pixel_time_value = nearest_ds['time'].values[row_index, col_index]

print(f"Single time value at the nearest pixel: {nearest_pixel_time_value}")

import pandas as pd

# Convert the nearest_pixel_time_value to a pandas Timestamp object
nearest_pixel_timestamp = pd.Timestamp(nearest_pixel_time_value)

# Format the pandas Timestamp object into a string
formatted_time_string = nearest_pixel_timestamp.strftime('%Y-%m-%d %H:%M')

# Print the formatted time string to verify the result
print(f"Formatted time string: {formatted_time_string}")

# Step 6: Plotting wind speed and direction using barbs


center_lat, center_lon = 20, 120

# Create a figure and axes with a PlateCarree projection
fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

# Add coastlines and countries
ax.coastlines()
ax.add_feature(cf.BORDERS, linestyle=':')
ax.add_feature(cf.STATES, linestyle=':')

# Add gridlines for reference
gl = ax.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.top_labels = False  # Turn off top labels
gl.right_labels = False # Turn off right labels

ax.set_extent([min_lon, max_lon, min_lat, max_lat], crs=ccrs.PlateCarree())

# Define color levels for wind speed
wind_speed_levels = np.arange(0, 80, 5)  # 0 to 75 in increments of 5

# Define custom colormap
colors = ['blue', 'green', 'yellow', 'red', 'purple', 'brown', 'pink']
cmap_name = 'ascat_cmap'
cm = mcolors.LinearSegmentedColormap.from_list(cmap_name, colors, N=len(wind_speed_levels)-1)

norm = mcolors.BoundaryNorm(wind_speed_levels, cm.N)


# Iterate through the opened datasets
for filename, ds in datasets.items():
    try:
        wind_speed = ds['wind_speed'] * 1.94384 #Convert to knots
        wind_dir = ds['wind_dir']
        lon = ds['lon']
        lat = ds['lat']

        # Convert wind direction from degrees to radians
        wind_dir_rad = np.deg2rad(wind_dir)

        # Calculate U and V components
        u_full = wind_speed * np.sin(wind_dir_rad)
        v_full = wind_speed * np.cos(wind_dir_rad)

        # Check if the dataset's spatial extent is within the desired bounds
        # Colorcode the barbs based on wind speed
        cs = ax.barbs(lon[:], lat[:], u_full.values, v_full.values, wind_speed.values,
                      cmap=cm, norm=norm, length=5) # Use custom colormap

    except KeyError as e:
        print(f"Error: Variable {e} not found in dataset {filename}")
    except Exception as e:
        print(f"Error processing dataset {filename}: {e}")

# Create the plot title with the wind information and the time of the nearest pixel
title_string = f'ASCAT 25km Winds | {satellite_search.upper()} | {formatted_time_string} UTC'


ax.set_title(title_string)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Add a colorbar
cbar = fig.colorbar(cs, ticks=wind_speed_levels)
cbar.set_label('Wind Speed (knots)')

plt.show()

# Close all opened datasets
for filename, ds in datasets.items():
    try:
        ds.close()
        print(f"Closed dataset: {filename}")
    except Exception as e:
        print(f"Error closing dataset {filename}: {e}")

print("All datasets have been closed.")

# Find all files starting with 'ascat_'
files_to_delete = glob.glob('ascat_*')
add_to_delete = glob.glob('*.xml')
files_to_delete.extend(add_to_delete)

print(f"Found {len(files_to_delete)} files to delete.")

# Delete each file
for file_path in files_to_delete:
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except OSError as e:
        print(f"Error deleting {file_path}: {e}")

print("Deletion process complete.")
