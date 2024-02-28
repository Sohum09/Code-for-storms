import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import datetime
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
print(cdx, "\n", cdy, "\n", winds, "\n", status, "\n", timeCheck, "\n", r34, "\n", DateTime)
#-----------------------------------------------------------------------------------


# Assuming DateTime, Winds, and Pressure are your arrays
# Example data (replace this with your actual data)

# Convert string datetime to datetime objects
DateTime = [datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in DateTime]

# Create a figure and axis
fig, ax1 = plt.subplots()

# Plotting Winds on the primary Y-axis (left)
ax1.set_xlabel('Date and Time')
ax1.set_ylabel('Winds (Kts)', color='tab:blue')
ax1.plot(DateTime, winds, color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a secondary Y-axis (right) for Pressure
ax2 = ax1.twinx()
ax2.set_ylabel('Pressure (hPa)', color='tab:red')
ax2.plot(DateTime, pres, color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Formatting date on the X-axis
date_form = DateFormatter('%Y-%m-%d')
ax1.xaxis.set_major_formatter(date_form)
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=24))

# Rotate and align the date labels so they look better
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha="right")

# Show the plot
plt.title(f'Intensity profile for {btkID}{yr}')
plt.tight_layout()
plt.show()
