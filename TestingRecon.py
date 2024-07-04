import urllib3
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
from datetime import datetime
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import matplotlib.transforms as transforms
import math
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)

def fetch_url(urlLink):
    response = http.request('GET', urlLink)
    return response.data.decode('utf-8')

def parse_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

url = "https://www.nhc.noaa.gov/text/URNT15-NOAA.shtml?text"

btk_data = fetch_url(url)
parsed_data = parse_data(btk_data)

lines = parsed_data.split('\n')

isValidData = 0
validData = []

def is_three_digit_number(s):
    pattern = r'^(?!.*\|)\d{3}$'
    return bool(re.match(pattern, s))

for line in lines:
    if line.strip():
        if line == "$$" or line.split()[0]=="Standard":
            isValidData = 0
            break
        if is_three_digit_number(line) or line=='000 ':
            isValidData = 1
        if isValidData != 1:
            validData.append(line)
        
reconHDOB = []
for i in range(12, len(validData)):  
    reconHDOB.append(validData[i])

for i in range(len(reconHDOB)):
    print(reconHDOB[i])

# Create the plot and set up the map
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

ax.coastlines()
ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')

# Define the color mapping for wind speeds
colors = ['b', 'g', '#ffff00', '#ffa001', '#ff5908', 'r', 'm']
bounds = [0, 34, 64, 81, 96, 112, 137, 200]
norm = mcolors.BoundaryNorm(bounds, len(colors))

def plot_wind_barb(ax, wind_speed, wind_direction, lat, lon, xtrap_val=0, sfmr='', flag=0):
    # Convert wind direction to radians
    wind_direction_rad = np.radians(wind_direction)
    
    # Calculate the u and v components of the wind vector
    u = wind_speed * np.sin(wind_direction_rad)
    v = wind_speed * np.cos(wind_direction_rad)
    
    if wind_speed >= 137:
        color = 'm'
    elif wind_speed >= 112:
        color = 'r'
    elif wind_speed >= 96:
        color = '#ff5908'
    elif wind_speed >= 81:
        color = '#ffa001'
    elif wind_speed >= 64:
        color = '#ffff00'
    elif wind_speed >= 34:
        color = 'g'
    else:
        color = 'b'

    # Plot the wind barb on the existing map
    ax.barbs(lon, lat, u, v, length=7, color=color, transform=ccrs.PlateCarree())
    ax.text(lon, lat+0.01, f'{xtrap_val}\n{sfmr}', transform=ccrs.PlateCarree(), fontsize=8, ha='center', va='center')
    if sfmr != '' and flag==1:
        ax.text(lon-0.01, lat+0.01, '!', color='r', transform=ccrs.PlateCarree(), fontsize=15, ha='center', va='center')

maxLat, minLat, maxLong, minLong = -999, 999, -999, 999
for data_line in reconHDOB:
    HDOBfix = data_line.split()
    print(HDOBfix)

    lat = float(HDOBfix[1][:2]) + float(HDOBfix[1][2:4])/60
    lon = float(HDOBfix[2][:3]) + float(HDOBfix[2][3:5])/60
    if HDOBfix[1][-1] == 'S':
        lat *= -1
    if HDOBfix[2][-1] == 'W':
        lon *= -1

    if(maxLat < lat):
        maxLat = lat
    if(minLat > lat):
        minLat = lat
    if(maxLong < lon):
        maxLong = lon
    if(minLong > lon):
        minLong = lon 
    
    fl_wind_dir = 180 + float(HDOBfix[8][:3])
    
    fl_wind_speed=''
    if fl_wind_speed == "///":
        continue

    fl_wind_speed = float(HDOBfix[9])

    sfmr = HDOBfix[10]
    print(sfmr)
    if sfmr == '///':
        sfmr = 'NaN'
    else:
        sfmr = int(sfmr)

    xtrap = HDOBfix[5]
    xtrap_val = 0
    if xtrap == '////':
        xtrap_val = ''
    elif xtrap[0] == '0':
        xtrap_val = 1000 + float(xtrap)/10
    else:
        xtrap_val = float(xtrap)/10

    flag=0
    if HDOBfix[-1][-1] in ['5', '6', '9']:
        flag=1
    print(lat, ", ", lon, ", ", fl_wind_dir, ", ", fl_wind_speed)
    
    plot_wind_barb(ax, fl_wind_speed, fl_wind_dir, lat, lon, xtrap_val, sfmr, flag)

def calculate_bearing(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Calculate the difference in longitude
    d_lon = lon2 - lon1
    
    # Calculate the bearing
    x = math.sin(d_lon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(d_lon))
    initial_bearing = math.atan2(x, y)
    
    # Convert bearing from radians to degrees
    initial_bearing = math.degrees(initial_bearing)
    
    # Normalize the bearing
    bearing = (initial_bearing + 360) % 360
    
    return bearing + 180

second_last = reconHDOB[-2].split()
seclast_lat = (float(second_last[1][:2]) + float(second_last[1][2:4])/60)
seclast_lat = seclast_lat*-1 if second_last[1][-1] == 'S' else seclast_lat
seclast_lon = (float(second_last[2][:3]) + float(second_last[2][3:5])/60)
seclast_lon = seclast_lon*-1 if second_last[2][-1] == 'W' else seclast_lon

plane_Loc = reconHDOB[-1].split()
plane_lat = (float(plane_Loc[1][:2]) + float(plane_Loc[1][2:4])/60)
plane_lat = plane_lat*-1 if plane_Loc[1][-1] == 'S' else plane_lat
plane_lon = (float(plane_Loc[2][:3]) + float(plane_Loc[2][3:5])/60)
plane_lon = plane_lon*-1 if plane_Loc[2][-1] == 'W' else plane_lat

degrees = calculate_bearing(seclast_lat, seclast_lon, plane_lat, plane_lon)

rotation = transforms.Affine2D().rotate_deg(degrees)
# Combine the rotation transformation with the current plot's transformation
transform = rotation + ax.transData

ax.plot(lon, lat, marker=(3, 0, degrees), markersize=20, transform=ax.transData, linestyle='None', color='k')

legend_elements = [Line2D([0], [0], marker='^', color='k', label='Last reported Aircaft Location',markerfacecolor='#444764', markersize=10),]

ax.set_extent([minLong-0.1, maxLong+0.1, minLat-0.1, maxLat+0.1], crs=ccrs.PlateCarree())

# Get the current UTC time
current_utc_time = datetime.utcnow()

plt.title(f'Test Recon Flight Data into AL022024 Beryl as of {current_utc_time} UTC')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Create the colorbar
cmap = mcolors.ListedColormap(colors)
norm = mcolors.BoundaryNorm(bounds, cmap.N)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
ax.legend(handles=legend_elements, loc='upper center')

# Add colorbar to the plot
cbar = plt.colorbar(sm, ticks=bounds, orientation='horizontal', pad=0.05, aspect=50, ax=ax, shrink=0.5)
cbar.set_label('30-sec recorded FL wind speed (Knots)')
cbar.ax.set_xticklabels(['0', '34', '64', '81', '96', '112', '137', '200'])

plt.show()
