import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)

def fetch_url(urlLink):
    response = http.request('GET', urlLink)
    return response.data.decode('utf-8')

def parse_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

btkID = input("Enter the Storm ID: ")
yr = input("Enter year: ")

if btkID[:2] in ['sh', 'wp', 'io']:
    btkUrl = f'https://www.ssd.noaa.gov/PS/TROP/DATA/ATCF/JTWC/b{btkID}{yr}.dat'
else:
    btkUrl = f'https://www.ssd.noaa.gov/PS/TROP/DATA/ATCF/NHC/b{btkID}{yr}.dat'

btk_data = fetch_url(btkUrl)
parsed_data = parse_data(btk_data)

lines = parsed_data.split('\n')

btk_parameters = lines[-2].split(',')
bt_list = []
for i in range(len(btk_parameters)):
    bt_list.append(btk_parameters[i].strip())

def calc_ACE(btkLines):
    ace = 0
    for line in btkLines:
        if line.strip():
            params = line.split(',')
            if(params[11].strip() == '34'):
                ace += (int(params[8]) ** 2) / 10000
    return ace


def decode_JTWC_btk(bt_list):
    coord_x = bt_list[6][:-2] + "." + bt_list[6][-2:]
    coord_y = bt_list[7][:-2] + "." + bt_list[7][-2:]
    print(f"\n\nATCF ID: {bt_list[0]}{bt_list[1]}{yr}")
    print(f"Name of Storm: {bt_list[10]} {bt_list[27]}")
    print(f"Time and Date: {bt_list[2][8:]}00 UTC, {bt_list[2][6:8]}/{bt_list[2][4:6]}/{bt_list[2][:4]}")
    print(f"Coordinates of center: {coord_x}, {coord_y}")
    print(f"\nCurrent Intensity: {bt_list[8]} Kts, {bt_list[9]} hPa")
    print(f"Current ACE upto this point: ", calc_ACE(lines))
    print(f"ENVP: {bt_list[17]} hPa")
    print(f"ROCI: {bt_list[18]} nm")
    print(f"RMW: {bt_list[19]} nm")

decode_JTWC_btk(bt_list)
