import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

filepath = 'woa23_all_o00mn01.csv'

data = []
with open(filepath, mode='r') as file:
    csvFile = csv.reader(file)
    for row in csvFile:
        if row[0].startswith('#'):
            continue
        
        lat = float(row[0])
        lon = float(row[1])
        
        # Filter for NIO area
        if 0 <= lat <= 40 and 50 <= lon <= 100:
            # take only surface value (col[2])
            if len(row) < 23:
                continue 
            #print(row[22])
            value = float(row[22]) if row[22].strip() != '' else np.nan
            data.append([lat, lon, value])

df = pd.DataFrame(data, columns=['lat', 'lon', 'O2_surface'])
print("Shape of DataFrame:", df.shape)
print(df.head())

# --- pivot into grid ---
df_grid = df.pivot(index='lat', columns='lon', values='O2_surface')

lat_unique = df_grid.index.values
lon_unique = df_grid.columns.values
oxygen_grid = df_grid.values  # now shape matches (lat, lon)

# --- plot ---
fig = plt.figure(figsize=(8,6))
ax = plt.axes(projection=ccrs.PlateCarree())

mesh = ax.pcolormesh(
    lon_unique, lat_unique, oxygen_grid,
    cmap="viridis", shading="auto",
    transform=ccrs.PlateCarree()
)

ax.coastlines(color='magenta')
ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
ax.add_feature(cfeature.BORDERS, linestyle=":")
ax.set_extent([50, 100, 0, 40], crs=ccrs.PlateCarree())

# colorbar
cbar = plt.colorbar(mesh, ax=ax, orientation="vertical", shrink=0.8, pad=0.07)
cbar.set_label("Dissolved Oxygen (ml/l) at 100 m")

ax.set_title("WOA23 Dissolved Oxygen (100m below Sea Level) — NIO Area")

plt.show()
