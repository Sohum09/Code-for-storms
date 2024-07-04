import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np

# Create the plot and set up the map
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
ax.coastlines()

def plot_wind_barb(ax, wind_speed, wind_direction, lat, lon):
    # Convert wind direction to radians
    wind_direction_rad = np.radians(wind_direction)
    
    # Calculate the u and v components of the wind vector
    u = wind_speed * np.sin(wind_direction_rad)
    v = wind_speed * np.cos(wind_direction_rad)
    
    # Plot the wind barb on the existing map
    ax.barbs(lon, lat, u, v, length=7, transform=ccrs.PlateCarree())

    # Optionally, you can customize further:
    # ax.set_title(f'Wind Barb: {wind_speed} knots at {wind_direction}°')
    # ax.set_xlabel('Longitude')
    # ax.set_ylabel('Latitude')

# Example wind barb plots
plot_wind_barb(ax, 103, 163, 17.21, -76.3)
plot_wind_barb(ax, 80, 250, 10, -160)
plot_wind_barb(ax, 120, 45, 0, 30)

plt.title('Multiple Wind Barbs')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
