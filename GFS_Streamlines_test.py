lat, lon = 20.94, -143.56
copy_lon = lon + 360 if lon < 0 else lon  # Ensure longitude is in the range [0, 360)
url = f'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?dir=%2Fgfs.20250813%2F12%2Fatmos&file=gfs.t12z.pgrb2.0p25.f000&var_UGRD=on&var_VGRD=on&lev_850_mb=on&lev_700_mb=on&lev_500_mb=on&lev_200_mb=on&subregion=&toplat={lat+10}&leftlon={copy_lon-10}&rightlon={copy_lon+10}&bottomlat={lat-10}'

import requests
filename = 'gfs_data'

try:
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check for HTTP errors

    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Data successfully downloaded to {filename}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while downloading the data: {e}")

# This code downloads GFS data for a specific latitude and longitude.
# It constructs the URL for the GFS data, ensuring the longitude is in the correct range.
# It then uses the requests library to fetch the data and save it to a file.

import xarray as xr
try:
    ds = xr.open_dataset(filename, engine='cfgrib')
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")

ds.to_netcdf('gfs_data.nc')
print("Data saved to gfs_data.nc")

u_wind, v_wind = ds['u'], ds['v']
longitude, latitude = ds['longitude'], ds['latitude']

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.style as mplstyle
mplstyle.use("dark_background") 

# Select data for 200mb pressure level
u_200mb, v_200mb = u_wind.sel(isobaricInhPa=200), v_wind.sel(isobaricInhPa=200)
longitude = xr.where(longitude < 0, longitude + 180, longitude - 180)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=180))
ax.set_extent([longitude.min(), longitude.max(), latitude.min(), latitude.max()], crs=ccrs.PlateCarree(central_longitude=180))
ax.add_feature(cfeature.COASTLINE, linewidth=1, color="c")
ax.add_feature(cfeature.BORDERS, color="w", linewidth=0.5)



# Plot streamlines
ax.streamplot(longitude, latitude, u_200mb.values, v_200mb.values, transform=ccrs.PlateCarree(central_longitude=180))

# Add coastlines and gridlines
ax.coastlines()
ax.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.7, linestyle='--')

# Add title
ax.set_title(f'GFS 200mb streamlines at ({lat}, {lon}), 2025-08-13 12:00 UTC')

# Display the plot
plt.show()

import os
import glob
os.remove(filename)  # Clean up the downloaded file
paths_to_remove = sorted(glob.glob('gfs_data.*'))
for path in paths_to_remove:
    os.remove(path)  # Clean up any additional files created by cfgrib

"""
Plan for bot integration:


"""