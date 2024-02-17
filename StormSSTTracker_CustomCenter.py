import urllib3
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.lines import Line2D
import numpy as np
import netCDF4

centerX, centerY = -79.2, 31.6

dataset = netCDF4.Dataset('oisst-avhrr-v02r01.20040801.nc')

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
    Line2D([0], [0], marker='x', color='k', label=f'Storm location',markerfacecolor='#444764', markersize=10),
    Line2D([0], [0], marker='_', color='k', label='26 degC SST Isotherm', markerfacecolor='#444764', markersize=10),
]

plt.scatter(centerX, centerY, color='k', marker='x', zorder=10000000)
ax.set_extent([centerX-10, centerX+10, centerY-10, centerY+10], crs=ccrs.PlateCarree())
plt.title(f'SST Map over storm')
ax.legend(handles=legend_elements, loc='upper center')
plt.show()