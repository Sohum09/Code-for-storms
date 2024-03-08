import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
from netCDF4 import Dataset
from matplotlib.colors import ListedColormap

#Example ERSST dataset
file_path = 'ersst.v5.202402.nc'
nc = Dataset(file_path, 'r')
from PIL import Image

lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]
ssta = nc.variables['ssta'][0, 0, :, :]


fig = plt.figure(figsize=(10, 6), dpi=200)


ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')

ax.add_feature(cfeature.COASTLINE, linewidth=0.8, edgecolor='black')
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='black')

lon_shifted = np.where(lon < 180, lon - 360, lon)

def image_to_hex_array(image_path, x_range, y_coord, exclude_colors):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Check if the array has an alpha channel
    if img_array.shape[2] == 4:
        # If alpha channel is present, remove it
        img_array = img_array[:, :, :3]

    # Extract colors from the specified coordinates
    colors = []
    for x in range(x_range[0], x_range[1] + 1):
        color = img_array[y_coord, x, :3]
        hex_color = '#%02x%02x%02x' % (color[0], color[1], color[2])

        # Exclude specified colors
        if hex_color not in exclude_colors:
            colors.append(hex_color)
    width, height = img.size
    print(width, height)
    return colors

# Specify extraction parameters
x_range = (52, 1084)
y_coord = 28

#Remove the black bars, as much as possible anyway
exclude_colors = ['#0b0004', '#280024', '#130016', '#4d418d', '#00000c', '#001377',
                  '#000412', '#00264f', '#004267', '#8e8e8e', '#2a2a2a', '#c4c4c4',
                  '#6d5a00', '#3f3300', '#1e1300', '#824000', '#1c0900', '#a92300',
                  '#970000', '#220400', '#881d00', '#420000', '#0b0000', '#8E8E8E',
                  '#262626', '#2A2A2A', '#747474', '#C4C4C4', '#6D5A00', '#E0B900',
                  '#6D5A00', '#181400', '#3F3300', '#B69400', '#E5BA00', '#AD6C00', 
                  '#1E1300', '#040200', '#824000', '#DB6C00', '#DA4A00', '#612100',
                  '#1C0900', '#4B1000', '#A92300', '#F23300', '#0086CF', '#004267', 
                  '#000A15', '#00264F', '#0060C7', '#0075F3', '#002BB7', '#000412',
                  '#000315', '#001377', '#001FC0']

# Extract colors
extracted_colors = image_to_hex_array('crw.png', x_range, y_coord, exclude_colors)

# Create the custom colormap
crw = ListedColormap(extracted_colors, name='crw')

# Plot the SST Anomaly data
pcm = ax.pcolormesh(lon, lat, ssta, transform=ccrs.PlateCarree(), cmap=crw, vmin=-5.1, vmax=5.1)

# Add colorbar
cbar = plt.colorbar(pcm, ax=ax, orientation='vertical', fraction=0.02)
cbar.set_label('Sea Surface Temperature Anomaly (°C)')

plt.title('Sea Surface Temperature Anomaly')

plt.show()

nc.close()

# Print the extracted colors
print(extracted_colors)
