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
    
    fl_wind_dir = float(HDOBfix[8][:3])
    fl_wind_speed=''
    if fl_wind_speed == "///":
        continue

    fl_wind_speed = float(HDOBfix[9])

    sfmr = HDOBfix[10]
    print(sfmr)
    if sfmr == '///':
        sfmr = ''
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

# Add colorbar to the plot
cbar = plt.colorbar(sm, ticks=bounds, orientation='horizontal', pad=0.05, aspect=50, ax=ax, shrink=0.5)
cbar.set_label('30-sec recorded FL wind speed (Knots)')
cbar.ax.set_xticklabels(['0', '34', '64', '81', '96', '112', '137', '200'])

plt.show()