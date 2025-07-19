import inspect
import cmap_collection

def _classify_colormaps():
    """Internal function to classify colormap functions based on vmax values."""
    wv_list = []  # Water vapor channel functions
    ir_list = []  # Infrared channel functions
    
    # Get all functions from the cmap_collection module
    functions = inspect.getmembers(cmap_collection, inspect.isfunction)
    
    for func_name, func_obj in functions:
        try:
            # Call the function to get colormap, vmax, vmin
            colormap, vmax, vmin = func_obj()
            
            # Classify based on vmax value
            if vmax < 293:
                wv_list.append(func_name)
            else:
                ir_list.append(func_name)
                
        except Exception as e:
            print(f"Error processing function {func_name}: {e}")
    
    return wv_list, ir_list

# Execute classification when module is imported
wv, ir = _classify_colormaps()

# Optional: Display results when run directly
if __name__ == "__main__":
    print("Water Vapor Channel Functions (vmax < 293):")
    for func in wv:
        print(f"  - {func}")
    
    print(f"\nInfrared Channel Functions (vmax >= 293):")
    for func in ir:
        print(f"  - {func}")
    
    print(f"\nTotal functions classified: {len(wv) + len(ir)}")
    print(f"Water vapor functions: {len(wv)}")
    print(f"Infrared functions: {len(ir)}")