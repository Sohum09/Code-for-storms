import cfgrib
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cdsapi

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
            'pressure_level': [
                '200', '850',
            ],
            'year': '2013',
            'day': '04',
            'month': '10',
            'time': '12:00',
            'area': [
                28, 123, 18,
                133,
            ],
        },
        'download.grib')

def read_grib_data(grib_file):
    ds = cfgrib.open_datasets(grib_file)

    u850_data, v850_data, u200_data, v200_data = None, None, None, None
    for dataset in ds:
        pressure_levels = dataset['isobaricInhPa'].values
        if 850 in pressure_levels:
            u850_data = dataset['u'].sel(isobaricInhPa=850).values
            v850_data = dataset['v'].sel(isobaricInhPa=850).values
        if 200 in pressure_levels:
            u200_data = dataset['u'].sel(isobaricInhPa=200).values
            v200_data = dataset['v'].sel(isobaricInhPa=200).values

    if u850_data is None or v850_data is None or u200_data is None or v200_data is None:
        raise ValueError("Could not find the required pressure levels in the GRIB file.")
    
    lats = ds[0]['latitude'].values
    lons = ds[0]['longitude'].values
    
    return lons, lats, u850_data, v850_data, u200_data, v200_data

def calculate_wind_shear(u850, v850, u200, v200):
    du = u200 - u850
    dv = v200 - v850
    shear_magnitude = np.sqrt(du**2 + dv**2) * 1.94384  # convert to knots
    return du, dv, shear_magnitude

def plot_wind_shear(lons, lats, du, dv, shear_magnitude):
    fig = plt.figure(figsize=(12, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    
    ax.set_extent([123, 133, 18, 28], crs=ccrs.PlateCarree())
    
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.LAND, edgecolor='black')
    ax.add_feature(cfeature.OCEAN, edgecolor='black')
    
    # Add grid lines
    ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle='--')
    
    # Plot the wind shear streamlines with color coding based on shear magnitude
    strm = ax.streamplot(lons, lats, du, dv, color=shear_magnitude, cmap='viridis', linewidth=1, transform=ccrs.PlateCarree())
    
    # Add a color bar, scaled to fit the plot size
    cbar = plt.colorbar(strm.lines, ax=ax, orientation='horizontal', pad=0.05, aspect=50, shrink=0.75)
    cbar.set_label('Vertical Wind Shear (knots)')
    
    plt.title('Deep Layer Vertical Wind Shear (200 hPa - 850 hPa)\n 12 PM UTC on October 4th, 2013')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    
    plt.show()

def main():
    # Step 1: Download data
    download_data()
    
    # Step 2: Proceed with the wind shear program
    lons, lats, u850_data, v850_data, u200_data, v200_data = read_grib_data('download.grib')
    du, dv, shear_magnitude = calculate_wind_shear(u850_data, v850_data, u200_data, v200_data)
    plot_wind_shear(lons, lats, du, dv, shear_magnitude)

if __name__ == "__main__":
    main()
