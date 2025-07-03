import json
import urllib3
from urllib.parse import quote

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)

sensors = ['amsr2', 'gmi', 'tms', 'ssmis']
products = ['89H', '91H']

sensor_str = ','.join(sensors)
product_str = ','.join(products)

url = f"https://science.nrlmry.navy.mil/geoips/prod_api/tcweb/products/2025?storm_id=wp042025&sensor=amsr2&sensor=gmi&sensor=tms&sensor=ssmis&product=89H&product=91H"

# Make the request
response = http.request('GET', url)

# Print raw response data for debugging
response_data = response.data.decode('utf-8')
print(f"Raw response data:", response_data)

# Check the content type
if response.headers.get('Content-Type') == 'application/json':
    try:
        # Parse the JSON response
        data = json.loads(response_data)
        #print(f"Parsed data", data)
        #print(data.get('data', [])) 
    except json.JSONDecodeError as e:
        print(f"JSON decode error:", e)
else:
    print(f"Unexpected content type for:", response.headers.get('Content-Type'))

from datetime import datetime

latest = max(
    data.get('products', []),
    key=lambda x: datetime.fromisoformat(x['product_date'])
)

print(f"Latest product: {latest['product']} from {latest['sensor']} on {latest['product_date']}")
print(f"URL: {latest['product_url']}")