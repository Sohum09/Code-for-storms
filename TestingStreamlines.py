import cdsapi
import cfgrib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Step 1: Download the data using the CDS API
def download_data():
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-pressure-levels',
        {
            'product_type': 'reanalysis',
            'format': 'grib',
            'variable': [
                'u_component_of_wind', 'v_component_of_wind',
            ],
            'pressure_level': '200',
            'year': '2013',
            'month': '10',
            'day': '04',
            'time': '12:00',
            'area': [
                28, 123, 18,
                133,
            ],
        },
        'download.grib')

# Step 2: Read and process the GRIB data
def read_grib_data(grib_file):
    ds = cfgrib.open_dataset(grib_file)
    u850_data = ds['u'].values
    v850_data = ds['v'].values
    
    lats = ds['latitude'].values
    lons = ds['longitude'].values
    
    return lons, lats, u850_data, v850_data

# Step 3: Plot the streamlines with color representing wind speed in knots
def plot_streamlines(lons, lats, u850_data, v850_data):
    # Calculate wind speed magnitude in m/s
    wind_speed_m_s = np.sqrt(u850_data**2 + v850_data**2)
    # Convert wind speed to knots
    wind_speed_knots = wind_speed_m_s * 1.94384
    
    fig = plt.figure(figsize=(12, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    
    ax.set_extent([are, 133, 18, 28], crs=ccrs.PlateCarree())
    
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.LAND, edgecolor='black')
    ax.add_feature(cfeature.OCEAN, edgecolor='black')
    
    # Add grid lines
    ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle='--')
    
    # Plot streamlines with color representing wind speed
    strm = ax.streamplot(lons, lats, u850_data, v850_data, transform=ccrs.PlateCarree(), linewidth=1, density=2,
                         color=wind_speed_knots, cmap='gist_ncar', arrowstyle='->', arrowsize=1.5)
    
    # Add a color bar, scaled to fit the plot size
    cbar = plt.colorbar(strm.lines, ax=ax, orientation='horizontal', pad=0.05, aspect=50, shrink=0.75)
    cbar.set_label('Wind Speed (knots)')
    
    plt.title('Streamlines of Winds at 200 hPa\n 12 PM UTC on October 4th, 2013')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    
    plt.show()

# Main function to execute the steps
def main():
    download_data()
    lons, lats, u850_data, v850_data = read_grib_data('download.grib')
    plot_streamlines(lons, lats, u850_data, v850_data)

if __name__ == "__main__":
    main()
