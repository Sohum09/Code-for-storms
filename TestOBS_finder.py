import pandas as pd

# Define the URL from which to load the CSV data
url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/osmc_rt_60.csv?platform_code,platform_type,latitude,longitude&latitude>=12.6&latitude<=14.6&longitude>=-115.6&longitude<=-113.6&distinct()"

# Read the CSV content from the URL
data = pd.read_csv(url)

# Display the content of the CSV
distinct_stations = data[['platform_code', 'platform_type', 'latitude', 'longitude']].drop_duplicates(subset='platform_code')

# Display the distinct platform codes along with their types, latitudes, and longitudes
print(distinct_stations)
