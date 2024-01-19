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

# Step 5: Display the parsed data
print(parsed_data)