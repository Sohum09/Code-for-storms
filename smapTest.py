import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from datetime import datetime
import requests
from io import BytesIO
import os
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)

def fetch_url(urlLink):
    response = http.request('GET', urlLink)
    return response.data.decode('utf-8')

def parse_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

btkID = input("Enter the Storm ID: ")

if btkID[:2] in ['sh', 'wp', 'io']:
    btkUrl = f'https://www.ssd.noaa.gov/PS/TROP/DATA/ATCF/JTWC/b{btkID}2024.dat'
else:
    btkUrl = f'https://www.ssd.noaa.gov/PS/TROP/DATA/ATCF/NHC/b{btkID}2024.dat'

btk_data = fetch_url(btkUrl)
parsed_data = parse_data(btk_data)

lines = parsed_data.split('\n')

cdx, cdy, winds, status, timeCheck, pres, DateTime, r34 = [], [], [], [], [], [], [], []
stormName = ""

for line in lines:
    if line.strip():
        parameters = line.split(',')
        if parameters[6][-1] == 'S':
            cdy.append((float(parameters[6][:-1].strip()) / 10)*-1)
        else:
            cdy.append(float(parameters[6][:-1].strip()) / 10)
    
        if parameters[7][-1] == 'W':
            cdx.append((float(parameters[7][:-1].strip()) / 10)*-1)
        else:
            cdx.append(float(parameters[7][:-1].strip()) / 10)


current_datetime = datetime.now()
year = str(current_datetime.year)
month = str(current_datetime.month).zfill(2)
day = str(current_datetime.day).zfill(2)

# Define the storm's coordinates
storm_lat = float(cdx[-1])  # Example latitude
storm_lon = float(cdy[-1])  # Example longitude

# Calculate latitude and longitude bounds for the bounding box
lat_min = storm_lat - 10
lat_max = storm_lat + 10
lon_min = storm_lon - 10
lon_max = storm_lon + 10

url = f'https://data.remss.com/smap/wind/L3/v01.0/daily/NRT/{year}/RSS_smap_wind_daily_{year}_{month}_{day}_NRT_v01.0.nc'

destination = f'smap{year}{month}.nc'

response = requests.get(url)
with open(destination, 'wb') as file:
    file.write(response.content)

# Open the NetCDF file using xarray
ds = xr.open_dataset(destination)

# Extract the wind variable
wind = ds['wind']
# Extract wind data within the bounding box
wind_bounded = wind.sel(lat=slice(lat_min, lat_max), lon=slice(lon_min, lon_max))

# Check if wind data is available within the bounding box
if len(wind_bounded.lat) == 0 or len(wind_bounded.lon) == 0:
    print("No data available within the bounding box.")
else:
    # Find the maximum wind value within the bounding box
    max_wind_value = wind_bounded.max()

    # Create the plot
    fig = plt.figure(figsize=(10, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())

    # Plot wind data using pcolormesh
    mesh = ax.pcolormesh(wind.lon, wind.lat, (wind.isel(node=1))*1.944, transform=ccrs.PlateCarree(), cmap='jet', vmin=0, vmax=150)
    contour = ax.contour(wind.lon, wind.lat, wind.isel(node=1), levels=[17], colors='black', transform=ccrs.PlateCarree())

    # Add coastlines
    ax.coastlines()

    # Add gridlines
    gls = ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
    gls.top_labels=False   # suppress top labels
    gls.right_labels=False # suppress right labels

    # Set the extent of the plot to zoom into the bounding box
    ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())

    # Add title
    plt.title('SMAP Ocean Surface Wind Speed', loc='left')

    # Add colorbar
    cbar = plt.colorbar(mesh, ax=ax, shrink=0.5, extend='both')
    cbar.set_label('Wind Speed (m/s)')
    # Print the maximum wind value within the bounding box
    max_wind_value = max_wind_value.values.item()*1.944  # Get the raw value

    def oneMin(raw_SMAP):
      processed_SMAP = (362.644732816453 * raw_SMAP + 2913.62505913216) / 380.88384339523

      #Display output:
      processed_SMAP = "{:.2f}".format(processed_SMAP)
      return processed_SMAP


    plt.title(f"Maximum 10-min wind value: {max_wind_value:.2f} kts, 1-min: {oneMin(max_wind_value)} kt", loc='right', fontsize=8)
    # Show the plot
    plt.show()
    ds.close()

    os.remove(destination)