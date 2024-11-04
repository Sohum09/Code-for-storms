import urllib3
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import numpy as np
import math

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)

url = 'https://www.psl.noaa.gov/mjo/mjoindex/omi.era5.1x.webpage.4023.txt'
day = int(input('Enter day: '))
month = int(input('Enter month: '))
year = int(input('Enter year: '))


def fetch_data(url):
    response = http.request('GET', url)
    return response.data.decode('utf-8')

def parse_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

mjo_data = fetch_data(url)
parsed_data = parse_data(mjo_data)

mjo_data = []
parsed_lines = parsed_data.split('\n')
i, limit = 0, 10
for line in parsed_lines:
    if line:
        mjo_data = line.split()
        if mjo_data[0] == str(year) and mjo_data[1] == str(month) and mjo_data[2] == str(day):
            break
        else:
            mjo_data = []

#Plot inner circle of suppresed MJO
circle = plt.Circle((0, 0), 1, fill=False)
fig, ax = plt.subplots()
ax.add_patch(circle)
plt.grid(color='gray', linestyle=':')
plt.axis('scaled')

#Plot MJO value
plt.scatter(float(mjo_data[4]), -1*float(mjo_data[3]), marker='o', color='r', s=45)
#          x (RMM PC1) = OMI PC2   y (RMM PC2) = - OMI PC1

#Plot the y = x line split
x1 = np.arange(-5, 1*math.cos(5*math.pi/4)+0.1, 0.1)
x2 = np.arange(1*math.cos(math.pi/4), 5, 0.1)
y1 = x1 # y = x
y2 = x2 # y = x
plt.plot(x1, y1, color='k') 
plt.plot(x2, y2, color='k') 

#Plot the y = -x line split
x3 = np.arange(-5, 1*math.cos(3*math.pi/4)+0.1, 0.1)
x4 = np.arange(1*math.cos(7*math.pi/4), 5, 0.1)
y3 = -x3
y4 = -x4
plt.plot(x3, y3, color='k') 
plt.plot(x4, y4, color='k') 

#Plot x-axis
x5 = np.arange(-5, -0.9, 0.1)
x6 = np.arange(1, 5, 0.1)
y5 = np.zeros_like(x5)
y6 = np.zeros_like(x6)
plt.plot(x5, y5, color='k') 
plt.plot(x6, y6, color='k') 

#Plot y-axis
x7 = np.arange(-5, -0.9, 0.1)
x8 = np.arange(1, 5, 0.1)
plt.plot(np.zeros_like(x7), x7, color='k')
plt.plot(np.zeros_like(x8), x8, color='k')

#Plot the phase numbers:
plt.text(-3.5, -1.33, '1')
plt.text(-1.5, -3.5, '2')
plt.text(1.5, -3.5, '3')
plt.text(3.5, -1.33, '4')
plt.text(3.5, 1.33, '5')
plt.text(1.5, 3.5, '6')
plt.text(-1.5, 3.5, '7')
plt.text(-3.5, 1.67, '8')

#Plot the region text:
plt.text(-0.7, -3.9, 'Indian\nOcean', color='green', size=12, fontweight='bold')
plt.text(-0.7, 3.2, 'Western\nPacific', color='magenta', size=12, fontweight='bold')
plt.text(-3.9, -1, 'Western Hem.\n& Africa', color='blue', size=12, rotation=90, fontweight='bold')
plt.text(3.1, -1, 'Maritime\nContinent', color='brown', size=12, rotation=270, fontweight='bold')

monthMap = {1:"January", 2: "February", 3:"March", 4:"April",
             5:"May", 6:"June", 7:"July", 8:"August",
             9: "September", 10:"October", 11:"November", 12:"December"}

plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.title(f'MJO Phase Diagram for {day} {monthMap[month]} {year}')
plt.xlabel("RMM PC1 component")
plt.ylabel("RMM PC2 component")
plt.show()