#Original code was created by Kathy Chan. Credits to her!
#Modified by Nino Morakot to fix some bugs in the code

import pandas as pd

NAME = "LOLA" #Enter name of the storm that you want to input
YEAR = 2024 #Enter year that the storm takes place in.

# Read all columns including wind field radii data
data_tc = pd.read_csv("bsh012024.dat", usecols=range(23), header=None)
data_tc.columns =['Hem', '#', 'Dt', '.', 'Best', 'O', 'Lat', 'Lon', 'Wind', 'Pressure', 'status',
                  'rad', 'windcode', 'rad1', 'rad2', 'rad3', 'rad4', 'pouter', 'router', 
                  'rmw', 'gusts', 'eye', 'subregion']

# Group by datetime to combine wind radii from different thresholds
grouped = data_tc.groupby('Dt')

# Process each unique time
results = []
for dt, group in grouped:
    # Get the main row (the one with rad=0, which has the basic track info)
    main_rows = group[group['rad'] == 0]
    if len(main_rows) > 0:
        main_row = main_rows.iloc[0].copy()
    else:
        main_row = group.iloc[0].copy()
    
    # Initialize wind radii as zeros
    rad34 = [0, 0, 0, 0]  # 34kt winds: NE, SE, SW, NW
    rad50 = [0, 0, 0, 0]  # 50kt winds
    rad64 = [0, 0, 0, 0]  # 64kt winds
    
    # Extract wind radii based on rad column
    for idx, row in group.iterrows():
        if row['rad'] == 34:
            rad34 = [row['rad1'], row['rad2'], row['rad3'], row['rad4']]
        elif row['rad'] == 50:
            rad50 = [row['rad1'], row['rad2'], row['rad3'], row['rad4']]
        elif row['rad'] == 64:
            rad64 = [row['rad1'], row['rad2'], row['rad3'], row['rad4']]
    
    main_row['rad34_1'] = rad34[0]
    main_row['rad34_2'] = rad34[1]
    main_row['rad34_3'] = rad34[2]
    main_row['rad34_4'] = rad34[3]
    main_row['rad50_1'] = rad50[0]
    main_row['rad50_2'] = rad50[1]
    main_row['rad50_3'] = rad50[2]
    main_row['rad50_4'] = rad50[3]
    main_row['rad64_1'] = rad64[0]
    main_row['rad64_2'] = rad64[1]
    main_row['rad64_3'] = rad64[2]
    main_row['rad64_4'] = rad64[3]
    
    results.append(main_row)

data_tc2 = pd.DataFrame(results)
m = data_tc2.shape[0]
D=100
data_tc2['date'] = data_tc2['Dt']//D
data_tc2['time'] = data_tc2['Dt']%D*100
data_tc2['time'] = data_tc2['time'].astype('string')
data_tc2['time'] = data_tc2['time'].apply(lambda x: '{:0>4}'.format(x))

# Convert lat/lon to proper decimal format (e.g., 685 -> 6.8S, 16870 -> 168.7E)
def format_latlon(coord_str):
    # Remove any non-digit characters except the last character (hemisphere)
    if coord_str[-1].isalpha():
        hemisphere = coord_str[-1]
        digits = coord_str[:-1]
    else:
        hemisphere = ''
        digits = coord_str
    
    # Insert decimal point before last digit
    if len(digits) >= 2:
        formatted = digits[:-1] + '.' + digits[-1]
    else:
        formatted = '0.' + digits
    
    return formatted + hemisphere

data_tc2['Lat'] = data_tc2['Lat'].apply(format_latlon)
data_tc2['Lon'] = data_tc2['Lon'].apply(format_latlon)

print(F"{data_tc2['Hem'].iloc[-1]}{data_tc2['#'].iloc[-1]}{YEAR}, {NAME:>18}, {m:5},")
for j in range(m):
    # Output with proper wind radii: 34kt (4 quadrants), 50kt (4 quadrants), 64kt (4 quadrants)
    HURDAT = F"{data_tc2['date'].iloc[j]}, {data_tc2['time'].iloc[j]},  ,{data_tc2['status'].iloc[j]},{data_tc2['Lat'].iloc[j]:>6},{data_tc2['Lon'].iloc[j]:>7}, {data_tc2['Wind'].iloc[j]:3}, {data_tc2['Pressure'].iloc[j]:4}, {int(data_tc2['rad34_1'].iloc[j]):4}, {int(data_tc2['rad34_2'].iloc[j]):4}, {int(data_tc2['rad34_3'].iloc[j]):4}, {int(data_tc2['rad34_4'].iloc[j]):4}, {int(data_tc2['rad50_1'].iloc[j]):4}, {int(data_tc2['rad50_2'].iloc[j]):4}, {int(data_tc2['rad50_3'].iloc[j]):4}, {int(data_tc2['rad50_4'].iloc[j]):4}, {int(data_tc2['rad64_1'].iloc[j]):4}, {int(data_tc2['rad64_2'].iloc[j]):4}, {int(data_tc2['rad64_3'].iloc[j]):4}, {int(data_tc2['rad64_4'].iloc[j]):4},"
    print(HURDAT)
