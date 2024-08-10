#URL: Enter here as per Step 3!
url = "https://noaa-nesdis-tcprimed-pds.s3.amazonaws.com/v01r00/final/2004/EP/13/TCPRIMED_v01r00-final_EP132004_AMSRE_AQUA_012577_20040913203813.nc"
#Enter 1 or 0 if you want to smoothen the output:
smooth = 0

import subprocess, sys, datetime, requests
packages = ["netCDF4", "matplotlib", "cartopy"]
for package in packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from scipy.ndimage import gaussian_filter
from matplotlib.tri import Triangulation, LinearTriInterpolator, CubicTriInterpolator
import numpy as np
plt.rcParams['pcolor.shading'] = 'auto'

url_response = requests.get(url)
FILE_NAME = "Output.nc"
DS = Dataset(FILE_NAME, memory=url_response.content)

#----------------------------------If using the Appendix, Paste in these bounds----------------------------------------------
#Select the variables per Step 4 and 5!
Strm_latitude = DS["passive_microwave/S6/latitude"][:]
Strm_longitude = DS["passive_microwave/S6/longitude"][:]
Strm = DS["passive_microwave/S6/TB_B89.0H"][:]
#----------------------------------------------------------------------------------------------------------------------------
color = "89" #Input either "89" or "37" depending on your color scale.


if smooth == 1:
  Strm_latitude_flat = Strm_latitude.flatten()
  Strm_longitude_flat = Strm_longitude.flatten()
  Strm_flat = Strm.flatten()

  triang = Triangulation(Strm_longitude_flat, Strm_latitude_flat)

  interpolator = LinearTriInterpolator(triang, Strm_flat)
  xi, yi = np.meshgrid(np.linspace(Strm_longitude_flat.min(), Strm_longitude_flat.max(), 500), np.linspace(Strm_latitude_flat.min(), Strm_latitude_flat.max(), 500))
  zi = interpolator(xi, yi)

  zi_smoothed = gaussian_filter(zi, sigma=1)

def mw89():
  newcmp = LinearSegmentedColormap.from_list("", [
    (0/100, '#0507b4'),
    (10/100, "#0457cf"),
    (20/100, "#06a5eb"),
    (26/100, "#0ad5c2"),
    (26/100, "#0bb617"),
    (30/100, "#20bc01"),
    (40/100, "#4fd200"),
    (50/100, "#80ec02"),
    (52/100, "#8ef101"),
    (52/100, "#f1e400"),
    (60/100, "#f2de01"),
    (68/100, "#f8c30d"),
    (68/100, "#f90602"),
    (70/100, "#f40a03"),
    (80/100, "#da280a"),
    (90/100, "#be4411"),
    (100/100, "#a36319"),])

  vmax = 280
  vmin = 180

  return newcmp.reversed(), vmax, vmin

def mw37():
  newcmp = LinearSegmentedColormap.from_list("", [
    (0/115, '#7f0102'),
    (5/115, '#9a1a02'),
    (15/115, "#d05102"),
    (25/115, "#fd8608"),
    (35/115, "#f5c141"),
    (45/115, "#e0c66e"),
    (55/115, "#98f68c"),
    (65/115, "#9fe4c9"),
    (75/115, "#60e0fe"),
    (85/115, "#24a4fe"),
    (95/115, "#106dee"),
    (105/115, "#4c33b3"),
    (115/115, "#7f017e"),])

  vmax = 280
  vmin = 165

  return newcmp.reversed(), vmax, vmin


name = [DS["overpass_metadata/basin"][:].item(), str(DS["overpass_metadata/cyclone_number"][:].item()).zfill(2), DS["overpass_metadata/season"][:].item()]
name = "".join(map(str, name))
instrument_name = DS["overpass_metadata/instrument_name"][:].item()

time = DS["overpass_metadata/time"][:].item()
dt = datetime.datetime.utcfromtimestamp(time)
formatted_time = dt.strftime('%d/%m %H:%M UTC')

Strm_longitude = (Strm_longitude + 180) % 360 - 180
col, vm, vn = mw89() if color == "89" else mw37()
if smooth == 0:
  plt.pcolormesh(Strm_longitude, Strm_latitude, Strm, cmap=col, vmax=vm, vmin=vn)
else:
  plt.pcolormesh(xi, yi, zi_smoothed, cmap=col, vmax=vm, vmin=vn)
plt.colorbar(label=f"Brightness Temperature (Kelvin)")

plt.title(f"{name} {formatted_time}\n{instrument_name} ~{color} GHz")


plt.grid(color='gray', linestyle=':')
plt.axis("scaled")
storm_latitude = DS["overpass_storm_metadata/storm_latitude"][:][0]
storm_longitude = DS["overpass_storm_metadata/storm_longitude"][:][0]
storm_longitude = (storm_longitude + 180)% 360 - 180
plt.xlabel("Longitude (degrees east)")
plt.ylabel("Latitude (degrees north)")
plt.xlim(storm_longitude - 5, storm_longitude + 5)
plt.ylim(storm_latitude - 5, storm_latitude + 5)
print("Longitude range after conversion:", Strm_longitude.min(), Strm_longitude.max())
