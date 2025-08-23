import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker
import matplotlib.style as mplstyle
import matplotlib.colors as mcolors
mplstyle.use("dark_background")

file_path = 'Test_ncep_uwind_anomaly.nc'
ds = xr.open_dataset(file_path)

print(ds)

zonal_mean = ds.uwnd.mean(dim='lon')
lon, lat = ds.lon, ds.lat
uwind_anomaly = ds.uwnd - zonal_mean
uwind_anomaly_2d = uwind_anomaly.squeeze()

fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree(central_longitude=180)}, figsize=(12, 10))

ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.LAND, facecolor='lightgray')

gl = ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
gl.top_labels = False   # suppress top labels
gl.right_labels = False  # suppress right labels
ax.set_extent([lon.min(), lon.max(), lat.min(), lat.max()], crs=ccrs.PlateCarree(central_longitude = 180))

# Normalization: center at 0
norm = mcolors.TwoSlopeNorm(
    vmin=uwind_anomaly_2d.min(),
    vcenter=0,
    vmax=uwind_anomaly_2d.max()
)

mesh = ax.pcolormesh(
    lon, lat, uwind_anomaly_2d,
    cmap='coolwarm',
    norm = norm,
    transform=ccrs.PlateCarree(),
    shading='auto'
)

# Shift longitude coords
uwind_anomaly_shifted = uwind_anomaly_2d.assign_coords(
    lon=(((uwind_anomaly_2d.lon + 180) % 360) - 180)
).sortby("lon")

# Highlight thresholds
for val, color in zip([-20, -15 -10, -5, 0, 5, 10, 15, 20], ["violet", "#0717f7", "blue", "#7982f7", "grey", "#f77979", "red", "#b81414", "crimson"]):
    cs = ax.contour(uwind_anomaly_shifted.lon, uwind_anomaly_shifted.lat, uwind_anomaly_shifted, levels=[val], colors=[color], linewidths=2, transform=ccrs.PlateCarree())
    ax.clabel(cs, fmt={val: f"{val}"}, inline=True, fontsize=10)
    
plt.colorbar(mesh, ax=ax, orientation='horizontal', pad=0.05, label='U-wind anomaly (m/s)')
plt.tight_layout()
plt.show()
