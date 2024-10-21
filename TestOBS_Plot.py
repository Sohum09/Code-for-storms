import pandas as pd
import matplotlib.pyplot as plt

# Define the URL from which to load the CSV data
url = f"https://data.pmel.noaa.gov/pmel/erddap/tabledap/osmc_rt_60.csv?platform_code,platform_type,latitude,longitude,time,slp&orderBy(%22time%22)&platform_code=%22{str(52202)}%22"

# Read the CSV content from the URL, keeping all rows
data = pd.read_csv(url)

# Drop the first row (index 0)
data = data.drop(index=0)

# Reset the index after dropping the row
data.reset_index(drop=True, inplace=True)

# Display the first few rows and the columns of the DataFrame
print(data.head())
print("Columns after reading CSV:", data.columns.tolist())

# Convert 'time' to datetime, handling UTC
data['time'] = pd.to_datetime(data['time'], utc=True)

# Convert 'slp' to numeric, forcing errors to NaN
data['slp'] = pd.to_numeric(data['slp'], errors='coerce')

# Drop rows where 'slp' is NaN
data_clean = data.dropna(subset=['slp'])

# Plotting the SLP vs Time
plt.figure(figsize=(12, 6))
plt.plot(data_clean['time'], data_clean['slp'], marker='o', linestyle='-', color='b')
plt.title('Time vs Sea Level Pressure (SLP) series of Station')
plt.xlabel('Time (Date)')
plt.ylabel('Sea Level Pressure (hPa)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
