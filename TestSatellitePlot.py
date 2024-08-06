import json
import urllib3
from datetime import datetime, timedelta
from urllib.parse import quote
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.cm as cm
import math

# Initialize the HTTP client
http = urllib3.PoolManager()

SATELLITES = ["29522", "35951", "28054", "27424", "25994", "39260", "43010", "41882",
              "38337", "38771", "43689", "54234", "43013", "33591", "28654", "37849",
              "39574", "56753", "56442", "56444", "56754", "39634"]

satelliteMap = {"28054":"DMSP F16", "29522":"DMSP F17", "35951":"DMSP F18", "27424":"AQUA",
                "25994": "TERRA", "39260":"FENGYUN 3C", "43010":"FENGYUN 3D", "41882":"FENGYUN 4A",
                "38337":"GCOM-W1", "38771":"METOP-B", "43689":"METOP-C", "54234":"NOAA 21", "43013":"NOAA 20",
                "33591":"NOAA 19", "28654":"NOAA 18", "37849":"SUOMI NPP", "39574":"GPM-CORE", 
                "56753":"TROPICS-03", "56442":"TROPICS-05", "56444":"TROPICS-06", "56754":"TROPICS-07", "39634":"SENTINEL-1A"}

# Define the geographic point
latitude = 13.6
longitude = -114.6

# Define the bounding box around the point
box_size = 10  # Bounding box size in degrees
upper_right = f"{latitude + box_size},{longitude + box_size}"
lower_left = f"{latitude - box_size},{longitude - box_size}"

# Get the current UTC time
now = datetime.utcnow()
start_time = now.strftime('%Y-%m-%dT%H:%M:%SZ')

# Calculate the end time (6 hours from now)
end_time = (now + timedelta(hours=6)).strftime('%Y-%m-%dT%H:%M:%SZ')

# Function to fetch data for a single satellite
def fetch_data_for_satellite(satellite):
    url = (
        f"http://sips.ssec.wisc.edu/orbnav/api/v1/overpass.json?"
        f"sat={quote(satellite)}"
        f"&start={quote(start_time)}&end={quote(end_time)}"
        f"&ur={quote(upper_right)}&ll={quote(lower_left)}"
    )
    
    # Make the request
    response = http.request('GET', url)
    
    # Print raw response data for debugging
    response_data = response.data.decode('utf-8')
    #print(f"Raw response data for {satellite}:", response_data)
    
    # Check the content type
    if response.headers.get('Content-Type') == 'application/json':
        try:
            # Parse the JSON response
            data = json.loads(response_data)
            #print(f"Parsed data for {satellite}:", data)
            return data.get('data', [])  # Return the parsed data list
        except json.JSONDecodeError as e:
            print(f"JSON decode error for {satellite}:", e)
            return None
    else:
        print(f"Unexpected content type for {satellite}:", response.headers.get('Content-Type'))
        return None

# Function to calculate distance between two coordinates
def haversine(lat1, lon1, lat2, lon2):
    radius = 6378.137  # Radius of the Earth in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius * c

# List to hold all overpass points
fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

# Use a colormap to get distinct colors
colors = cm.tab20.colors

for idx, satellite in enumerate(SATELLITES):
    data = fetch_data_for_satellite(satellite)
    if data:
        color = colors[idx % len(colors)]  # Get a color from the colormap
        lats, lons = [], []
        min_distance = float('inf')
        min_distance_point = None
        min_distance_date = None
        
        for point in data:
            try:
                lat, lon = float(point[2]), float(point[3])
                if -90 <= lat <= 90 and -180 <= lon <= 180:
                    distance = haversine(latitude, longitude, lat, lon)
                    if distance <= 400 and distance < min_distance:
                        min_distance = distance
                        min_distance_point = (lat, lon)
                        min_distance_date = datetime.strptime(point[0], '%Y-%m-%dT%H:%M:%SZ').strftime('%d/%m\n%H:%M Z')
                        ax.plot(lon, lat, 'o', color=color, markersize=2)
                    lats.append(lat)
                    lons.append(lon)
                    
            except ValueError as e:
                print(f"ValueError for point {point}: {e}")

        if lats and lons and min_distance_point:
            ax.plot(lons, lats, color=color, linewidth=1, linestyle='-', alpha=0.7, label=satelliteMap.get(satellite, satellite))
        
        if min_distance_point:
            min_lat, min_lon = min_distance_point
            ax.plot(min_lon, min_lat, 'x', color='r', markersize=5)
            ax.text(min_lon, min_lat, min_distance_date, fontsize=8, color='red', ha='right')

ax.plot(longitude, latitude, 'x', color='k', markersize=5)
# Set map extent to show the area of interest
ax.set_extent([longitude - 5, longitude + 5, latitude - 5, latitude + 5])
gls = ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
gls.top_labels = False   # suppress top labels
gls.right_labels = False  # suppress right labels
plt.title("Satellite Overpass Points and Paths")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small', ncol=1, title='Satellites')
plt.show()
