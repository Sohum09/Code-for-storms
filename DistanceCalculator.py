#Script to calculate the distance between two coordinates on Earth in km.
import math

#Take inputs, converting them to radians in the process:
print("Enter the coordinates below! Use negatives for southern latitudes and WHEM longitudes.")
print("\nx here is latitude, y here is longitude.")
x1 = float(input("x1 in degrees = ")) * 0.0174533
y1 = float(input("y1 in degrees = ")) * 0.0174533
x2 = float(input("x2 in degrees = ")) * 0.0174533
y2 = float(input("y2 in degrees = ")) * 0.0174533

radius = 6378.137 #Assumed radius of the planet

#Apply the equation:
delY = y2 - y1
d_km = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(delY))

d_nm = d_km * 0.539957 #Finding the equivalent in nautical miles

#Print the output:
d_km = "{:.2f}".format(d_km)
d_nm = "{:.2f}".format(d_nm)
print("Distance in km: ", d_km, "km, in nautical miles: ", d_nm, "nm")
