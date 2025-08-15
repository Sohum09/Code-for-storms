#Disclaimer: The research by JWT is unpublished and not to be used in an operational setting!
import numpy as np
def return_ratio(fl_rmw): #Linear regression
    return -0.0024 * fl_rmw + 1.002
    
def rmw_curve_ratio(fl_rmw): #Log regression
    # fl_rmw in km
    a = 1.07047
    b = -0.050037
    return a + b * np.log(fl_rmw)

for i in range(5, 55+1, 5):
    print(f'Ratio for {i} km FL RMW = {return_ratio(i):.2f}')

print()

for i in range(5, 55+1, 5):
    print(f'Log Ratio for {i} km FL RMW = {rmw_curve_ratio(i):.2f}')
    
print(f'{rmw_curve_ratio(2.7):.2f}')