import urllib3
import netCDF4
import os


local_filename = "so26chgt_control_monthly_highres_2D_202110_OPER_v0.1.nc"

# Open the netCDF file and read its metadata and variables
dataset = netCDF4.Dataset(local_filename, 'r')

# Print the metadata
print("Metadata for:", local_filename)
for attr in dataset.ncattrs():
    print(f"{attr}: {getattr(dataset, attr)}")

print("\nVariables:")
for var_name in dataset.variables:
    var = dataset.variables[var_name]
    print(f"\nVariable: {var_name}")
    print(f"Dimensions: {var.dimensions}")
    print(f"Shape: {var.shape}")
    for var_attr in var.ncattrs():
        print(f"  {var_attr}: {getattr(var, var_attr)}")

# Close the dataset
dataset.close()

# Clean up the local file (optional)
os.remove(local_filename)
