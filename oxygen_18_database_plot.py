import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr
import numpy as np

filepath = r'C:\Users\USER\Downloads\calculated_d18O_v1_1.nc'

ds = xr.open_dataset(filepath)
#print(ds)

lat, lon = ds["lat"], ds["lon"]

d18o = ds["d18o"].sel(depth=0)

d18o_kerala = d18o.sel(
    lat=slice(0, 30),   # northward increasing, so slice(8,12)
    lon=slice(50, 100)   # eastward longitudes
)

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([50, 100, 0, 30], crs=ccrs.PlateCarree())
ax.coastlines(color='magenta')
ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
im = ax.pcolormesh(
    d18o_kerala["lon"],
    d18o_kerala["lat"],
    d18o_kerala,
    transform=ccrs.PlateCarree(),
    cmap='viridis'
)
plt.colorbar(im, ax=ax, orientation='horizontal', pad=0.05, label='d18O (‰)')

plt.title(f"Calculated Oxygen levels at {0} m for Indian Ocean Region – {ds.attrs['authors']}")
plt.show()