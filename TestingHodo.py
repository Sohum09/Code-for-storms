import cdsapi
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from metpy.calc import wind_speed
from metpy.plots import Hodograph
from metpy.units import units
import metpy.calc as mpcalc
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.style as mplstyle
from mpl_toolkits.axes_grid1 import make_axes_locatable
mplstyle.use("dark_background") 

# === 1. Retrieve ERA5 Wind Data === #
def retrieve_era5_hodograph(year, month, day, hour, lat_north, lon_west, lat_south, lon_east):
    client = cdsapi.Client()
    
    dataset = "reanalysis-era5-pressure-levels"
    request = {
        "product_type": "reanalysis",
        "variable": ["u_component_of_wind", "v_component_of_wind"],
        "pressure_level": ["1000", "950", "900", "850", "800", "750", "700", "650", "600", "550", "500", "450", "400", "350", "300" ,"250", "200", "150", "100"],  
        "year": str(year),
        "month": str(month).zfill(2),
        "day": str(day).zfill(2),
        "time": f"{hour}:00",
        "format": "netcdf",
        "area": [lat_north, lon_west, lat_south, lon_east],  # North, West, South, East
    }
    
    filename = "ERA5_hodograph.nc"
    client.retrieve(dataset, request, filename)
    return filename

# === 2. Process Data and Create Hodograph === #
def plot_hodograph(nc_file, lat, lon, date):
    # Load data
    ds = xr.open_dataset(nc_file)
    
    # Debug: Print dataset info
    #print(ds)
    # Assign units using Pint accessor
    ds = ds.metpy.quantify()

    # Ensure wind components have correct units
    ds["u"] = ds["u"].metpy.convert_units("knots")
    ds["v"] = ds["v"].metpy.convert_units("knots")

    # Compute mean wind components
    u_wind = ds["u"].mean(dim=["latitude", "longitude"])
    v_wind = ds["v"].mean(dim=["latitude", "longitude"])

    # Extract pressure levels
    pressure_levels = ds["pressure_level"].metpy.convert_units("hPa")

    # === Create Hodograph Plot === #
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_title(f"ECMWF ERAv5 plotted Hodograph centered over ({lat}, {lon})\n{date}, 5x5° Area-Averaged Grid with calculated shear vectors", fontsize=7, fontweight="bold")

    # Hodograph setup
    max_wind = max(
    abs(u_wind.metpy.convert_units("knots").values.max()),
    abs(v_wind.metpy.convert_units("knots").values.max()),
    abs(u_wind.metpy.convert_units("knots").values.min()),
    abs(v_wind.metpy.convert_units("knots").values.min())
    )
    hodo = Hodograph(ax, component_range=max_wind + 5)
    hodo.add_grid(increment=10)  # Add gridlines every 10 knots

    # Plot wind data
    hodo.plot(u_wind, v_wind, marker="o", markersize=1, linestyle="-", color="b", label="Wind Profile")

    # Create colormap based on pressure
    cmap = cm.get_cmap("Spectral_r")
    norm = mcolors.Normalize(vmin=pressure_levels.min(), vmax=pressure_levels.max())

    # Plot wind data with colored lines and black points
    for i in range(len(pressure_levels) - 1):
        u1, v1 = u_wind.isel(pressure_level=i).values.item(), v_wind.isel(pressure_level=i).values.item()
        u2, v2 = u_wind.isel(pressure_level=i+1).values.item(), v_wind.isel(pressure_level=i+1).values.item()
        
        # Colored line segment
        ax.plot([u1, u2], [v1, v2], color=cmap(norm(pressure_levels[i].values)), linewidth=2)

    for i, level in enumerate(ds["pressure_level"].values):
        if level in [850, 700, 500, 350, 200]:  # Only annotate these levels
            u_value = u_wind.isel(pressure_level=i).values.item()
            v_value = v_wind.isel(pressure_level=i).values.item()
            
            ax.scatter(u_value, v_value, s=30, edgecolor="white", linewidth=0.7)
            ax.text(
                u_value,
                v_value,
                f"{level:.0f} hPa",
                fontsize=10,
                ha="center"
            )
    # Create a divider for the axis to position the colorbar
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)  # Adjust size and padding
    # Add colorbar for reference
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, cax=cax, orientation="vertical", label="Pressure Level (hPa)")
    ax.set_xlabel("U-wind (knots)", fontsize=12)
    ax.set_ylabel("V-wind (knots)", fontsize=12)

    # === Compute and Plot Shear Vectors === #
    shear_layers = {
        "200–850 hPa": (200, 850),
        "500–850 hPa": (500, 850),
        "200–500 hPa": (200, 500),
        "300–800 hPa": (300, 800),
        "850–1000 hPa": (850, 1000),
    }

    import matplotlib.patches as mpatches
    from matplotlib.patches import FancyArrowPatch
    from matplotlib.legend_handler import HandlerPatch
    from matplotlib.lines import Line2D
    max_shear = []
    class HandlerArrow(HandlerPatch):
        def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
            # Calculate the center of the arrow
            center = height / 2.0

            # Use a valid color (e.g., white) explicitly
            color = "white"

            # Create the FancyArrowPatch for the legend
            p = FancyArrowPatch(
                (xdescent + width * 0.2, center),  # Start point
                (xdescent + width * 0.8, center),  # End point
                mutation_scale=15,  # Scale of arrow
                color=color,         # Explicitly set valid color
                arrowstyle="->"      # Define arrow style explicitly
            )
            p.set_transform(trans)
            return [p]


    legend_elements = []

    arrow_length_display = 5  # fixed visual arrow length
    arrow_color = "white"

    for label, (lower, upper) in shear_layers.items():
        u_lower = u_wind.sel(pressure_level=lower).values.item()
        v_lower = v_wind.sel(pressure_level=lower).values.item()
        u_upper = u_wind.sel(pressure_level=upper).values.item()
        v_upper = v_wind.sel(pressure_level=upper).values.item()

        shear_u = u_upper - u_lower
        shear_v = v_upper - v_lower
        shear_mag = np.sqrt(shear_u**2 + shear_v**2)
        max_shear.append(shear_mag)
        ax.quiver(
        u_lower, v_lower,    # Starting point (lower pressure level)
        shear_u, shear_v,    # Components (direction and magnitude)
        angles="xy", scale_units="xy", scale=1, color="#808080", width=0.002, linestyle="--"
        )

        # Normalize for fixed arrow direction
        unit_u = shear_u / shear_mag
        unit_v = shear_v / shear_mag

        scaled_u = unit_u * arrow_length_display
        scaled_v = unit_v * arrow_length_display

        # Create a custom arrow legend handle
        arrow = FancyArrowPatch(
            (0, 0), (shear_u, shear_v),  # unit direction
            color="white",
            arrowstyle='->',
            mutation_scale=15,
            lw=2
        )
        legend_elements.append(
            (arrow, f"{label}: {shear_mag:.1f} kt")
        )
    legend_elements.append(
            (arrow, f"Max shear: {max(max_shear):.1f} kt")
    )
    # Unpack handles and labels
    handles, labels = zip(*legend_elements)
    ax.legend(
        handles, labels,
        loc="lower center",
        fontsize=8,
        frameon=True,
        ncol=2,
        handler_map={FancyArrowPatch: HandlerArrow()}
    )



    plt.show()

# === 3. Run Everything === #
year, month, day, hour = 2019, 10, 7, 12
lat, lon = 25, 130
lat_north, lon_west, lat_south, lon_east = lat+2.5, lon-2.5, lat-2.5, lon+2.5  # Define 5×5 grid

#nc_file = retrieve_era5_hodograph(year, month, day, hour, lat_north, lon_west, lat_south, lon_east)
plot_hodograph("ERA5_hodograph.nc", lat, lon, f"{str(day).zfill(2)}/{str(month).zfill(2)}/{str(year)} at {str(hour)}00 UTC")
