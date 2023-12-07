import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

# Format: ["Abbreviated Month/Day/Year/UTC", 700mb Height in metres, Observed pressure] 
# Use None if data is not available for that particular point.
data = [
    ["Jun 17 1981 0619", None, 995],
    ["Jun 18 1981 0047", 3029, None],
    ["Jun 18 1981 0243", 2947, 984],
    ["Jun 18 1981 1310", 2846, None],
    ["Jun 18 1981 1603", 2842, 971],
    ["Jun 19 1981 0016", 2812, None],
    ["Jun 19 1981 0252", 2806, 967],
    ["Jun 19 1981 1246", 2775, None],
    ["Jun 19 1981 1430", 2782, 963],
    ["Jun 20 1981 0152", 2766, None],
    ["Jun 20 1981 0348", 2787, 963],
]

# Extracting data for plotting:
dates = [datetime.strptime(row[0], "%b %d %Y %H%M") for row in data]
observed_pressure = [row[2] for row in data]
converted_pressure = [645 + 0.115 * row[1] if row[1] is not None else None for row in data]

# Plotting:
plt.figure(figsize=(10, 6))
observed_line, = plt.plot(dates, observed_pressure, marker='o', linestyle='-', color='blue', label='Observed Pressure')
converted_line, = plt.plot(dates, converted_pressure, marker='s', linestyle='--', color='orange', label='Converted Pressure from 700mb Height')

# Adding text on plot for the datapoints:
for i, txt in enumerate(observed_pressure):
    if txt is not None:
        plt.annotate(str(txt), (dates[i], txt), textcoords="offset points", xytext=(0,-15), ha='center', color=observed_line.get_color())

for i, txt in enumerate(converted_pressure):
    if txt is not None:
        plt.annotate(str(round(txt, 2)), (dates[i], txt), textcoords="offset points", xytext=(0,10), ha='center', color=converted_line.get_color())

plt.xlabel('Date+Time (UTC)')
plt.ylabel('Pressure (mb)')
plt.title('Recon data for 05W TY June 1981')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
