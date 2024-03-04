import csv
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from datetime import datetime

#Initialize the script by creating the inquiry....
btkID = input("Enter the Storm ID: ")
yr = input("Enter year: ")
btkID = btkID.upper()
#Load in the loops for finding the latitude and longitude...
IBTRACS_ID = f"{btkID}{yr}"
cdx, cdy, winds, status, timeCheck, DateTime, pres = [], [], [], [], [], [], []
storm_name = ""
s_ID = ""
vmax = -999
#Template to read the IBTRACS Data...
with open('ibtracs.ALL.list.v04r00.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for line_num, lines in enumerate(csvFile, start=1):
        if line_num > 3:
            #Process or print the lines from the 4th line onwards
            #If IBTRACS ID matches the ID on the script...
            if lines[18] == IBTRACS_ID or (btkID == lines[5] and yr == lines[6][:4]):
                DateTime.append(lines[6])
                s_ID = lines[18]
                cdx.append(lines[20])
                cdy.append(lines[19])
                if int(yr) < 2002:
                    if lines[23] == ' ':
                        winds.append(15)
                    else:
                        winds.append(int(lines[23]))
                    if lines[11] == ' ':
                        pres.append(1010)
                    else:
                        pres.append(int(lines[11]))
                    if (vmax< int(winds[-1])):
                        vmax = int(winds[-1])
                else:
                    if lines[23] == ' ':
                        winds.append(15)
                    else:
                        winds.append(int(lines[23]))
                    if lines[24] == ' ':
                        pres.append(1010)
                    else:
                        pres.append(int(lines[24]))
                    if (vmax< int(winds[-1])):
                        vmax = int(winds[-1])
                status.append(lines[22])
                timeCheck.append(lines[6][-8:-6])
                storm_name = lines[5]
    
#-------------------------------DEBUG INFORMATION-----------------------------------
print(DateTime, "\n", winds, "\n", pres, "\n", storm_name)
#-----------------------------------------------------------------------------------


# Assuming DateTime, Winds, and Pressure are your arrays
# Example data (replace this with your actual data)

# Convert string datetime to datetime objects

DateTimePlot = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in DateTime]

# Create a figure and axis
fig, ax1 = plt.subplots()

# Plotting Winds on the primary Y-axis (left)
ax1.set_xlabel('Date and Time')
ax1.set_ylabel('Winds (Kts)', color='tab:blue')
ax1.plot(DateTimePlot, winds, color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

if int(yr) > 2002:
    # Create a secondary Y-axis (right) for Pressure
    ax2 = ax1.twinx()
    ax2.set_ylabel('Pressure (hPa)', color='tab:red')
    ax2.plot(DateTimePlot, pres, color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

# Formatting date on the X-axis
date_form = DateFormatter('%Y-%m-%d')
ax1.xaxis.set_major_formatter(date_form)
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=24))

#Building the function that calculates ACE...
def calc_ACE(winds, timeCheck):
    ace = 0
   
    for i in range(len(winds)):
        if(winds[i] == ' '):
            continue
        time = int(timeCheck[i]) % 6
        if(time==0 and int(winds[i]) >= 34 and status[i] not in ['DB', 'LO', 'WV', 'EX']): #If it is synoptic time and meets...
           ace += (int(winds[i]) ** 2) / 10000
    return "{:.4f}".format(ace)

# Rotate and align the date labels so they look better
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha="right")

# Show the plot
plt.title(f'{btkID} {yr}', loc='center')
plt.title(f'VMAX: {vmax} Kts', loc='left', fontsize=9)
plt.title(f'ACE: {calc_ACE(winds, timeCheck)}', loc='right', fontsize=9)
plt.tight_layout()
plt.grid(True)
plt.show()
