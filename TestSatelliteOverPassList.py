import json
import urllib3
from datetime import datetime, timedelta
from urllib.parse import quote

# Initialize the HTTP client
http = urllib3.PoolManager()

SATELLITES = ["40376", "29522", "35951", "28054", "27424", "25994", "39260", "43010", "41882",
              "38337", "38771", "43689", "54234", "43013", "33591", "28654", "37849",
              "39574", "56753", "56442", "56444", "56754"]

satelliteMap = {"28054":"DMSP F16", "29522":"DMSP F17", "35951":"DMSP F18", "27424":"AQUA",
                "25994": "TERRA", "39260":"FENGYUN 3C", "43010":"FENGYUN 3D", "41882":"FENGYUN 4A",
                "38337":"GCOM-W1", "38771":"METOP-B", "43689":"METOP-C", "54234":"NOAA 21", "43013":"NOAA 20",
                "33591":"NOAA 19", "28654":"NOAA 18", "37849":"SUOMI NPP", "39574":"GPM-CORE", 
                "56753":"TROPICS-03", "56442":"TROPICS-05", "56444":"TROPICS-06", "56754":"TROPICS-07"}

# Define the geographic point
latitude = 13.6
longitude = -114.6

# Define the bounding box around the point
# You can adjust the size of the bounding box if needed
box_size = 5  # Bounding box size in degrees
upper_right = f"{latitude + box_size},{longitude + box_size}"
lower_left = f"{latitude - box_size},{longitude - box_size}"

# Get the current UTC time
now = datetime.utcnow()
start_time = now.strftime('%Y-%m-%dT%H:%M:%SZ')  # Format: 2023-08-06T15:30:00Z

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
    print(f"Raw response data for {satellite}:", response_data)
    
    # Check the content type
    if response.headers.get('Content-Type') == 'application/json':
        try:
            # Parse the JSON response
            data = json.loads(response_data)
            print(f"Parsed data for {satellite}:", data)
        except json.JSONDecodeError as e:
            print(f"JSON decode error for {satellite}:", e)
    else:
        print(f"Unexpected content type for {satellite}:", response.headers.get('Content-Type'))

# Fetch data for each satellite
for satellite in SATELLITES:
    fetch_data_for_satellite(satellite)
