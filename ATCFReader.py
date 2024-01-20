import urllib3
from bs4 import BeautifulSoup

# Step 1: As the ATCF URL has a bugged SSL certificate, the following workarounds are needed: 
# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Explicitly disable SSL verification
http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)

# URL of the ATCF data
atcf_url = 'https://www.nrlmry.navy.mil/tcdat/sectors/atcf_sector_file'

# Step 2: Fetch ATCF data:
def fetch_atcf_data(url):
    response = http.request('GET', url)
    return response.data.decode('utf-8')

# Step 3: Display the ATCF data: 
def parse_atcf_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

# Step 4: Fetch and parse ATCF data
atcf_data = fetch_atcf_data(atcf_url)
parsed_data = parse_atcf_data(atcf_data)

# Step 5: Display the parsed data in encoded format:
print("Encoded ATCF Data:\n")
print(parsed_data)
print("\n")

# Step 6: We will now display the data by decoding it:
def displayStormInfo(storm_data):
    print("Decoded information from the ATCF: \n")
    basin_list = {
        'L': "North Atlantic Ocean", 
        'E': "East Pacific Ocean", 
        'C': "Central Pacific Ocean", 
        'W': "Western Pacific Ocean", 
        'A': "Arabian Sea",
        'B': "Bay of Bengal",
        'S': "South Indian Ocean",
        'P': "South Pacific Ocean"
        }
    def getBasin(sid):
        return basin_list[sid[-1]]
    for storm in storm_data:
        print("-----------------------------------")
        print(f"Storm ID: {storm['atcf_id']}")
        print(f"Name of Storm: {storm['name']}")
        print(f"Date of Reading: {storm['date']}")
        print(f"Time of Reading: {storm['hour']} UTC")
        print(f"Coordinates: {storm['latitude']}, {storm['longitude']}")
        print(f"Basin: {storm['basin']} - {getBasin(storm['atcf_id'])}")
        print(f"Intensity: {storm['winds']} Kts / {storm['pressure']} hPa")

#Step 7: To allow the function in Step 6 to work, we will now work on decoding the ATCF data:
storm_data = []
lines = parsed_data.split('\n')

for line in lines:
    if line.strip():
        parts = line.split(' ')
        storm_data.append({
            'atcf_id': parts[0],
            'name': parts[1],
            'date': f"{parts[2][4:]}-{parts[2][2:4]}-{parts[2][:2]}",
            'hour': parts[3],
            'latitude': parts[4],
            'longitude': parts[5],
            'basin': parts[6],
            'winds': parts[7],
            'pressure': parts[8]
        })

#Step 8: We conclude Steps 6 and 7 to display the decoded data:
displayStormInfo(storm_data)
