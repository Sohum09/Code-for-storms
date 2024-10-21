import cfgrib

def access_grib_metadata(grib_file):
    # Open the GRIB file using cfgrib
    try:
        ds = cfgrib.open_dataset(grib_file)
    except Exception as e:
        print(f"Error opening file: {e}")
        return

    # Print dataset information
    print("---- Global Attributes ----")
    for attr in ds.attrs:
        print(f"{attr}: {ds.attrs[attr]}")

    print("\n---- Data Variables ----")
    for var in ds.variables:
        print(f"Variable: {var}")
        print(f"Shape: {ds[var].shape}")
        print(f"Dimensions: {ds[var].dims}")
        print(f"Attributes: {ds[var].attrs}\n")

    # Additional metadata can be accessed like this
    print("\n---- Coordinate Variables ----")
    for coord in ds.coords:
        print(f"Coordinate: {coord}")
        print(f"Values: {ds[coord].values}\n")

if __name__ == "__main__":
    # Specify the path to your GRIB file here
    grib_file = "download.grib"
    access_grib_metadata(grib_file)
