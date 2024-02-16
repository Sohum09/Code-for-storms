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

        winds.append(int(parameters[8].strip()))
        status.append(parameters[10].strip())
        timeCheck.append((parameters[2][-2:].strip()))
        date = parameters[2].strip()
        date = f'{date[:4]}-{date[4:6]}-{date[6:8]} {timeCheck[-1]}:00:00'
        DateTime.append(date)
        pres.append(int(parameters[9].strip()))
        r34.append(int(parameters[11].strip()))
        stormName = parameters[27].strip()

#-------------------------------DEBUG INFORMATION-----------------------------------
print(cdx, "\n", cdy, "\n", winds, "\n", status, "\n", timeCheck, "\n", r34)
#-----------------------------------------------------------------------------------

#Beginning work on the actual plotting of the data:
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree(central_longitude=180)}, figsize=(12, 10))

ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
maxLat, minLat, maxLong, minLong = -999, 999, -999, 999
vmax, statMaxIndx = 0, 0

#Plotting the markers...
for i in range(0, len(cdx)):
    if cdx[i] == ' ' or cdy[i] == ' ' or winds[i] == ' ':
       continue
    
    coord_x, coord_y = float(cdx[i])+180 if float(cdx[i])<0 else float(cdx[i])-180, float(cdy[i])
    wind = int(winds[i])

    #Setup for finding bounding box...
    if(maxLat < coord_y):
        maxLat = coord_y
    if(minLat > coord_y):
        minLat = coord_y
    if(maxLong < coord_x):
        maxLong = coord_x
    if(minLong > coord_x):
        minLong = coord_x 
    
    #Setup for displaying VMAX as well as peak Status...
    if vmax < wind:
        vmax = wind
        statMaxIndx = i

    if(int(timeCheck[i]) % 6  == 0):
        #Mark scatter plots...
        if status[i] in ['DB', 'WV', 'LO', 'MD']:
            plt.scatter(coord_x, coord_y, color='#444764', marker='^')
        elif status[i] == 'EX':
            if int(wind) >= 64:
                plt.scatter(coord_x, coord_y, color='#ffff00', marker='^')
            elif int(wind) >= 34:
                plt.scatter(coord_x, coord_y, color='g', marker='^')
            else:
                plt.scatter(coord_x, coord_y, color='b', marker='^')
        elif status[i] == 'SS':
            plt.scatter(coord_x, coord_y, color='g', marker='s')
        elif status[i] == 'SD':
            plt.scatter(coord_x, coord_y, color='b', marker='s')
        else:
            if int(wind) >= 137:
                plt.scatter(coord_x, coord_y, color='m', marker='o')
            elif int(wind) >= 112:
                plt.scatter(coord_x, coord_y, color='r', marker='o')
            elif int(wind) >= 96:
                plt.scatter(coord_x, coord_y, color='#ff5908', marker='o')
            elif int(wind) >= 81:
                plt.scatter(coord_x, coord_y, color='#ffa001', marker='o')
            elif int(wind) >= 64:
                plt.scatter(coord_x, coord_y, color='#ffff00', marker='o')
            elif int(wind) >= 34:
                plt.scatter(coord_x, coord_y, color='g', marker='o')
            else:
                plt.scatter(coord_x, coord_y, color='b', marker='o')

#Setting the coordinates for the bounding box...
center_x = (minLong + maxLong)/2
center_y = (minLat + maxLat)/2

center_width = abs(maxLong - minLong)
center_height = abs(maxLat - minLat)

ratio = (center_height/center_width)
print(ratio)
if ratio < 0.3:
    ax.set_xlim(center_x-center_width, center_x+center_width)
    ax.set_ylim(center_y-(center_width/2), center_y+(center_width/2))
elif ratio > 0.7:
    ax.set_xlim(center_x-(center_height), center_x+(center_height))
    ax.set_ylim(center_y-center_height, center_y+center_height)
else:
    ax.set_xlim(center_x-center_width, center_x+center_width)
    ax.set_ylim(center_y-center_height, center_y+center_height)

#Defining the legend box for the plot...
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


#Building the function that calculates ACE...
def calc_ACE(winds, timeCheck):
    ace = 0
    aceList = []
    for i in range(len(winds)):
        if(winds[i] == ' '):
            continue
        time = int(timeCheck[i]) % 6 #If it is synoptic time and meets...
        if(time==0 and r34[i] == 34 and status[i] not in ['DB', 'LO', 'WV', 'EX']): 
           ace += (int(winds[i]) ** 2) / 10000
           aceList.append(ace)
    print(aceList)
    return "{:.4f}".format(ace)


#Plotting the TC Path...
LineX = []
LineY = []

for i in range(len(cdx)):
    if cdx[i] == ' ' or cdy[i] == ' ':
        continue
    LineX.append(float(cdx[i])+180 if float(cdx[i])<0 else float(cdx[i])-180)
    LineY.append(float(cdy[i]))

plt.plot(LineX, LineY, color="k", linestyle="--")
plt.text(LineX[0], LineY[0]+0.5, f'{DateTime[0]}')
plt.text(LineX[len(LineX)-1], LineY[len(LineX)-1]+0.5, f'{DateTime[len(LineX)-1]}')

#Applying final touches...
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title(f'{btkID.upper()}{yr} {stormName}')
plt.title(f'VMAX: {vmax} Kts', loc='left', fontsize=9)
plt.title(f'ACE: {calc_ACE(winds, timeCheck)}', loc='right', fontsize=9)
ax.legend(handles=legend_elements, loc='upper right')
plt.grid(True)
plt.show()
