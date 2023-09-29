import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Generate data points for the hurricane path - For the users!
num_points = 9
#The timed points are [Init, T+12, T+24, T+36, T+48, T+60, T+72, T+96, T+120] in hours per the lists.
latitudes = [18.4, 19.1, 19.6, 19.9, 20.4, 21.0, 22.0, 24.5, 27.0]
longitudes = [-46.6, -47.3, -48.3, -49.4, -50.7, -52.4, -54.1, -57.0, -57.0]
forecast_winds = [40, 65, 90, 110, 135, 140, 115, 95, -70] #In knots, -ve sign means that the system is not tropical.

#-------------------------------------------------No need to touch the below-----------------------------------------------

# Create a figure and axis with a specific map projection (e.g., PlateCarree)
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(12, 10))

# Plot the world map using Cartopy's features
ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

# Add latitude and longitude gridlines
ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')

# Plot the hurricane path
plt.plot(longitudes, latitudes, 'w-', label='TC Path')

# Create a cone of uncertainty around the path
cone_radius = [0.4, 0.43, 0.65, 0.88, 1.12, 1.35, 1.65, 2.42, 3.42]
count = 9
dupl = []
for i in range(num_points):
    if forecast_winds[i] < 0: #Non-tropical points
      circle = plt.Circle((longitudes[i], latitudes[i]), cone_radius[i], color='w', alpha=0.2, transform=ccrs.PlateCarree())
      count = -2
      if count not in dupl:
        plt.scatter(longitudes[i], latitudes[i], color='w', marker='*', label='Not Tropical')
        dupl.append(count)
      else:
        plt.scatter(longitudes[i], latitudes[i], color='w', marker='*')
      ax.add_patch(circle)

    elif forecast_winds[i] >= 140: #C5
      circle = plt.Circle((longitudes[i], latitudes[i]), cone_radius[i], color='m', alpha=0.2, transform=ccrs.PlateCarree())
      count = 5
      if count not in dupl:
        plt.scatter(longitudes[i], latitudes[i], color='m', marker='o', label='Category 5')
        dupl.append(count)
      else:
        plt.scatter(longitudes[i], latitudes[i], color='m', marker='o')
      ax.add_patch(circle)

    elif forecast_winds[i] >= 115: #C4
      circle = plt.Circle((longitudes[i], latitudes[i]), cone_radius[i], color='r', alpha=0.2, transform=ccrs.PlateCarree())
      count = 4
      if count not in dupl:
        plt.scatter(longitudes[i], latitudes[i], color='r', marker='o', label='Category 4')
        dupl.append(count)
      else:
        plt.scatter(longitudes[i], latitudes[i], color='r', marker='o')
      ax.add_patch(circle)

    elif forecast_winds[i] >= 100: #C3
      circle = plt.Circle((longitudes[i], latitudes[i]), cone_radius[i], color='#ff5908', alpha=0.2, transform=ccrs.PlateCarree())
      count = 3
      if count not in dupl:
        plt.scatter(longitudes[i], latitudes[i], color='#ff5908', marker='o', label='Category 3')
        dupl.append(count)
      else:
        plt.scatter(longitudes[i], latitudes[i], color='#ff5908', marker='o')
      ax.add_patch(circle)

    elif forecast_winds[i] >= 85: #C2
      circle = plt.Circle((longitudes[i], latitudes[i]), cone_radius[i], color='#ffa001', alpha=0.2, transform=ccrs.PlateCarree())
      count = 2
      if count not in dupl:
        plt.scatter(longitudes[i], latitudes[i], color='#ffa001', marker='o', label='Category 2')
        dupl.append(count)
      else:
        plt.scatter(longitudes[i], latitudes[i], color='#ffa001', marker='o')
      ax.add_patch(circle)

    elif forecast_winds[i] >= 65: #C1
      circle = plt.Circle((longitudes[i], latitudes[i]), cone_radius[i], color='y', alpha=0.2, transform=ccrs.PlateCarree())
      count = 1
      if count not in dupl:
        plt.scatter(longitudes[i], latitudes[i], color='y', marker='o', label='Category 1')
        dupl.append(count)
      else:
        plt.scatter(longitudes[i], latitudes[i], color='y', marker='o')
      ax.add_patch(circle)

    elif forecast_winds[i] >= 35: #TS
      circle = plt.Circle((longitudes[i], latitudes[i]), cone_radius[i], color='g', alpha=0.2, transform=ccrs.PlateCarree())
      count = 0
      if count not in dupl:
        plt.scatter(longitudes[i], latitudes[i], color='g', marker='o', label='Tropical Storm')
        dupl.append(count)
      else:
        plt.scatter(longitudes[i], latitudes[i], color='g', marker='o')
      ax.add_patch(circle)
      
    else: #TD
      circle = plt.Circle((longitudes[i], latitudes[i]), cone_radius[i], color='b', alpha=0.2, transform=ccrs.PlateCarree())
      count = -1
      if count not in dupl: 
        plt.scatter(longitudes[i], latitudes[i], color='b', marker='o', label='Tropical Depression')
        dupl.append(count)
      else:
        plt.scatter(longitudes[i], latitudes[i], color='b', marker='o')
      ax.add_patch(circle)

#------------------------------------------------You can now resume editing the cone------------------------------------------------

# Set axis limits
ax.set_xlim(-80, -20)
ax.set_ylim(0, 40)

# Add labels and legend
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Hurricane Forecast Cone Test: AL182023 RINA 03Z September 29')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
