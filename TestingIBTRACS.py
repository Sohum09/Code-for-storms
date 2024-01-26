import csv
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.lines import Line2D

#Initialize the script by creating the inquiry....
btkID = input("Enter the Storm ID: ")
yr = input("Enter year: ")

#Load in the loops for finding the latitude and longitude...
IBTRACS_ID = f"{btkID}{yr}"
cdx, cdy, winds, status, timeCheck = [], [], [], [], []
storm_name = ""
s_ID = ""
#Template to read the IBTRACS Data...
with open('ibtracs.ALL.list.v04r00.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for line_num, lines in enumerate(csvFile, start=1):
        if line_num > 3:
            #Process or print the lines from the 4th line onwards
            #If IBTRACS ID matches the ID on the script...
            if lines[18] == IBTRACS_ID or (btkID == lines[5] and yr == lines[6][:4]):
                s_ID = lines[18]
                cdx.append(lines[20])
                cdy.append(lines[19])
                winds.append(lines[23])
                status.append(lines[22])
                timeCheck.append(lines[6][-8:-6])
                storm_name = lines[5]
    
#-------------------------------DEBUG INFORMATION-----------------------------------
print(cdx, "\n", cdy, "\n", winds, "\n", status, "\n", timeCheck, "\n", storm_name)
#-----------------------------------------------------------------------------------

#Beginning work on the actual plotting of the data:
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(12, 10))

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

    coord_x, coord_y = float(cdx[i]), float(cdy[i])
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
            plt.scatter(coord_x, coord_y, color='g', marker='s')
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
    LineX.append(float(cdx[i]))
    LineY.append(float(cdy[i]))

plt.plot(LineX, LineY, color="k", linestyle="--")

#Applying final touches...
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title(f'{s_ID} {storm_name}')
plt.title(f'VMAX: {vmax} Kts', loc='left', fontsize=9)
plt.title(f'ACE: {calc_ACE(winds, timeCheck)}', loc='right', fontsize=9)
ax.legend(handles=legend_elements, loc='upper right' if btkID[:2]=="SH" or btkID[:2]=="EP" else "upper left")
plt.grid(True)
plt.show()
