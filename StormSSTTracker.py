import urllib3
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.lines import Line2D
import numpy as np
import netCDF4

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)

def fetch_url(urlLink):
    response = http.request('GET', urlLink)
    return response.data.decode('utf-8')

def parse_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

btkID = input("Enter the Storm ID: ")
yr = input("Enter year: ")

if btkID[:2] in ['sh', 'wp', 'io']:
    btkUrl = f'https://www.ssd.noaa.gov/PS/TROP/DATA/ATCF/JTWC/b{btkID}{yr}.dat'
else:
    btkUrl = f'https://www.ssd.noaa.gov/PS/TROP/DATA/ATCF/NHC/b{btkID}{yr}.dat'

btk_data = fetch_url(btkUrl)
parsed_data = parse_data(btk_data)
lines = parsed_data.split('\n')
cdx, cdy, DateTime, timeCheck = [], [], [], []
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
        timeCheck.append((parameters[2][-2:].strip()))
        date = parameters[2].strip()
        date = f'{date[:4]}-{date[4:6]}-{date[6:8]} {timeCheck[-1]}:00:00'
        DateTime.append(date)
        stormName = parameters[27].strip()

centerX, centerY = cdx[-1], cdy[-1]

dataset = netCDF4.Dataset('oisst-avhrr-v02r01.20240215_preliminary.nc')

# Extract latitude, longitude, and SST data
lat = dataset.variables['lat'][:]
lon = dataset.variables['lon'][:]
sst = dataset.variables['sst'][0, 0, :, :]  # Assuming time and zlev dimensions are 1

# Plotting the world map
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
ax.coastlines()
gls = ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
gls.top_labels=False   # suppress top labels
gls.right_labels=False # suppress right labels

# Plot SST data from 10 degC to 35 degC
c = ax.contourf(lon, lat, sst, levels=np.arange(10, 35, 1), transform=ccrs.PlateCarree(), cmap='coolwarm', extend='both')
# Add small contour lines for all SSTs
contour = ax.contour(lon, lat, sst, levels=np.arange(10, 35, 1), colors='black', linewidths=0.5, transform=ccrs.PlateCarree())
# Add a contour line for 26 degrees Celsius
contour_level = 26
contour = ax.contour(lon, lat, sst, levels=[contour_level], colors='black', linewidths=2, transform=ccrs.PlateCarree())

plt.colorbar(c, label='Sea Surface Temperature (°C)')

legend_elements = [
    Line2D([0], [0], marker='x', color='k', label=f'Storm location as of {DateTime[-1]}',markerfacecolor='#444764', markersize=10),
    Line2D([0], [0], marker='_', color='k', label='26 degC SST Isotherm', markerfacecolor='#444764', markersize=10),
]

plt.scatter(centerX, centerY, color='k', marker='x', zorder=10000000)
ax.set_extent([centerX-10, centerX+10, centerY-10, centerY+10], crs=ccrs.PlateCarree())
plt.title(f'SST Map over {btkID.upper()}{yr} {stormName}:')
ax.legend(handles=legend_elements, loc='upper center')
plt.show()