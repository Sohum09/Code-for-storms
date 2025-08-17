import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr
import numpy as np

filepath = r'C:\Users\USER\Downloads\poes.NOAA-4.halftone.north.VIS.1975.11.19.nc' #Place your downloaded file data here

ds = xr.open_dataset(filepath)

print(ds)
print(ds["crs"].attrs)
# Extract data
vis = ds["vis_norm_remapped"].squeeze()
x = ds["x"].values
y = ds["y"].values

# Define projection (guessing north pole stereo; check attrs for proj params)
crs = ccrs.Stereographic(
    central_latitude=90,
    central_longitude=-80,
    true_scale_latitude=90,
    globe=ccrs.Globe(ellipse=None, semimajor_axis=6371128.0, semiminor_axis=6371128.0)
)

# Plot
fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection=crs)




# Add coastlines for reference
ax.coastlines(color="yellow")

# Plot image in projection coordinates
im = ax.pcolormesh(x, y, vis, transform=crs, cmap="gray")

plt.colorbar(im, ax=ax, orientation="horizontal", pad=0.05, label="Brightness")
plt.title(f"NOAA-4 VIS – Polar Stereographic – {str(ds.time.values[0])}")
plt.show()