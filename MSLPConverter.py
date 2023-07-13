#Script to convert recorded pressure at an altitude to Sea Level Pressure.
#Reference link for the script: https://keisan.casio.com/keisan/image/Convertpressure.pdf

#Input parameters
altitude = float(input("Enter altitude of the recorded pressure in metres above sea level: "))
temperature =  float(input("Enter the recorded temperature at the observation in Celcius: "))
pressure = float(input("Enter the recorded pressure in mb/hPa: "))

#Apply the standard WMO equation:

p0 = pressure * (1 - ((0.0065 * altitude)/(temperature + 273.15 + 0.0065 * altitude))) ** (-5.257)

#Present the output in a readable manner:
pr = "{:.2f}".format(p0)
print("The equivalent sea level pressure: ", pr, "mb/hPa")
