import urllib3
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.lines import Line2D

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

fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(12, 10))

ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
maxLat, minLat, maxLong, minLong = -999, 999, -999, 999
vmax = 0

bt_list = []
cdx, cdy = [], []

for line in lines:
  if line.strip():
    params = line.split(',')
    for i in range(len(params)):
      bt_list.append(params[i].strip())
    coord_y = float(bt_list[6][:-2] + "." + bt_list[6][-2:-1])
    coord_x = float(bt_list[7][:-2] + "." + bt_list[7][-2:-1])
    
    if(params[6][-1] == 'S'):
      coord_y *= -1
    if(params[7][-1] == 'W'):
      coord_x *= -1
    cdx.append(coord_x)
    cdy.append(coord_y)

    if(maxLat < coord_y):
      maxLat = coord_y
    if(minLat > coord_y):
      minLat = coord_y
    if(maxLong < coord_x):
      maxLong = coord_x
    if(minLong > coord_x):
      minLong = coord_x 

    if vmax < int(bt_list[8]):
      vmax = int(bt_list[8])

    bt_list = []

plt.plot(cdx, cdy, color="k", linestyle="--", label='TC Path')

for line in lines:
  if line.strip():
    para = line.split(',')
    bt_list = []
    for i in range(len(para)):
      bt_list.append(para[i].strip())

    coord_y = float(bt_list[6][:-2] + "." + bt_list[6][-2:-1])
    coord_x = float(bt_list[7][:-2] + "." + bt_list[7][-2:-1])

    if(params[6][-1] == 'S'):
      coord_y *= -1
    if(params[7][-1] == 'W'):
      coord_x *= -1

    if bt_list[10] in ['DB', 'WV', 'LO', 'MD']:
      plt.scatter(coord_x, coord_y, color='#444764', marker='^')
    elif bt_list[10] == 'EX':
      if int(bt_list[8]) >= 64:
        plt.scatter(coord_x, coord_y, color='#ffff00', marker='^')
      elif int(bt_list[8]) >= 34:
        plt.scatter(coord_x, coord_y, color='g', marker='^')
      else:
        plt.scatter(coord_x, coord_y, color='b', marker='^')
    elif bt_list[10] == 'SS':
      plt.scatter(coord_x, coord_y, color='g', marker='s')
    elif bt_list[10] == 'SD':
      plt.scatter(coord_x, coord_y, color='b', marker='s')
    else:
      if int(bt_list[8]) >= 137:
        plt.scatter(coord_x, coord_y, color='m', marker='o')
      elif int(bt_list[8]) >= 112:
        plt.scatter(coord_x, coord_y, color='r', marker='o')
      elif int(bt_list[8]) >= 96:
        plt.scatter(coord_x, coord_y, color='#ff5908', marker='o')
      elif int(bt_list[8]) >= 81:
        plt.scatter(coord_x, coord_y, color='#ffa001', marker='o')
      elif int(bt_list[8]) >= 64:
        plt.scatter(coord_x, coord_y, color='#ffff00', marker='o')
      elif int(bt_list[8]) >= 34:
        plt.scatter(coord_x, coord_y, color='g', marker='o')
      else:
        plt.scatter(coord_x, coord_y, color='b', marker='o')

center_x = (minLong + maxLong)/2
center_y = (minLat + maxLat)/2

center_width = abs(maxLong - minLong)
center_height = abs(maxLat - minLat)

ratio = (center_height/center_width)
print(ratio)
if ratio < 0.3:
  ax.set_xlim(center_x-center_width, center_x+center_width)
  ax.set_ylim(center_y-(center_width/2), center_y+(center_width/2))
elif ratio>0.7:
  ax.set_xlim(center_x-(center_height), center_x+(center_height))
  ax.set_ylim(center_y-center_height, center_y+center_height)
else:
  ax.set_xlim(center_x-center_width, center_x+center_width)
  ax.set_ylim(center_y-center_height, center_y+center_height)

legend_elements = [
                  Line2D([0], [0], marker='^', color='w', label='Non-Tropical',markerfacecolor='#444764', markersize=10),
                  Line2D([0], [0], marker='s', color='w', label='Sub-Tropical',markerfacecolor='#444764', markersize=10),
                  Line2D([0], [0], marker='o', color='w', label='Tropical Depression',markerfacecolor='b', markersize=10),
                  Line2D([0], [0], marker='o', color='w', label='Tropical Storm',markerfacecolor='g', markersize=10),
                  Line2D([0], [0], marker='o', color='w', label='Category 1',markerfacecolor='#ffff00', markersize=10),
                  Line2D([0], [0], marker='o', color='w', label='Category 2',markerfacecolor='#ffa001', markersize=10),
                  Line2D([0], [0], marker='o', color='w', label='Category 3',markerfacecolor='#ff5908', markersize=10),
                  Line2D([0], [0], marker='o', color='w', label='Category 4',markerfacecolor='r', markersize=10),
                  Line2D([0], [0], marker='o', color='w', label='Category 5',markerfacecolor='m', markersize=10),
]

def calc_ACE(btkLines):
    ace = 0
    for line in btkLines:
        if line.strip():
            params = line.split(',')
            if(params[11].strip() == '34' and params[10].strip() not in ['DB', 'LO', 'EX', 'WV']):
                ace += (int(params[8]) ** 2) / 10000
    return "{:.4f}".format(ace)

# Add labels and legend
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title(f'Cyclone Best Track Test: {btkID}{yr}')
plt.title(f'VMAX: {vmax} Kts', loc='left', fontsize=9)
plt.title(f'ACE: {calc_ACE(lines)}', loc='right', fontsize=9)
ax.legend(handles=legend_elements, loc='upper right' if btkID[:2]=="sh" or btkID[:2]=="ep" else "upper left")
plt.grid(True)
plt.show()
