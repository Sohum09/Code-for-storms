import csv
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.lines import Line2D

#Loading in relevant variables....
cdx, cdy, winds, status, timeCheck,  pres = [], [], [], [], [], []

#Template to open HURDAT based files....
with open('StormTrack.txt', mode='r') as file:
    lines = (file.read()).split('\n')
    for line in lines:
        stormData = line.split(',')

        #Checking Longitudinal Hemisphere...
        if(stormData[5][-1] == 'W'):
            cdx.append(float(stormData[5][:-1].strip())*-1)
        else:
            cdx.append(float(stormData[5][:-1].strip()))
        
        #Checking Latitudinal Hemisphere...
        if(stormData[4][-1] == 'S'):
            cdy.append(float(stormData[4][:-1].strip())*-1)
        else:
            cdy.append(float(stormData[4][:-1].strip()))
        
        status.append(stormData[3].strip())
        winds.append(int(stormData[6].strip()))
        pres.append(int(stormData[7].strip()))
        stormData[1] = stormData[1].strip() #Bugfix
        timeCheck.append(int(stormData[1][:2]))
    
#---------------------------DEBUG INFORMATION--------------------------------
print(cdx, "\n", cdy, "\n", winds, '\n', pres, '\n', timeCheck, '\n', status)
#----------------------------------------------------------------------------

#Beginning work on the actual plotting of the data:
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree(central_longitude=180)}, figsize=(12, 10))

ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
maxLat, minLat, maxLong, minLong = -999, 999, -999, 999
vmax, pmin = 0, 9999

#Plotting the markers...
for i in range(len(cdx)):
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
    if pmin > pres[i]:
        pmin = pres[i]
    
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
   
    for i in range(len(winds)-1):
        if(winds[i] == ' '):
            continue
        time = int(timeCheck[i]) % 6
        if(time==0 and int(winds[i]) >= 34 and status[i] not in ['DB', 'LO', 'WV', 'EX']): #If it is synoptic time and meets...
           ace += (int(winds[i]) ** 2) / 10000
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

#Applying final touches...
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title(f'Peak Intensity: {vmax} Kts, {pmin} hPa', loc='left')
plt.title(f'ACE: {calc_ACE(winds, timeCheck)}', loc='right')
ax.legend(handles=legend_elements, loc='upper right')
plt.grid(True)
plt.show()
