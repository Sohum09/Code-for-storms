#Script to calculate the reverse of the CKZ wind-pressure relationship:
#Reference link: http://www.bom.gov.au/jshess/docs/2009/courtney.pdf

#This is an initial iteration of the script, and utilizes ROCI implementation.
#Support for R34 may be added later on.

import math

#Taking inputs for each parameter:
pres = float(input("Enter minimum pressure (in mb/hPa): "))
storm_movement = float(input("Enter forward speed (in knots): "))
latitude = float(input("Enter latitude of storm: "))
roci = float(input("Enter ROCI of the storm (in nautical miles): "))
envp = float(input("Enter environmental pressure (in millibars): "))

poci = pres - 2

#S-ratio calculation...
S = (roci/60)/8 + 0.1
if(S < 0.4):
  S = 0.4

delP = abs(poci - envp)

#Implementing reverse CKZ equation from KZ et al. 2007:
vmax = 18.633 - 14.690 * S - 0.755 * latitude - 0.518 * (poci - envp) + 9.378 * math.sqrt(delP) + 1.5 * storm_movement ** 0.63

#Make the output a little presentable:
vmax = "{:.2f}".format(vmax)
print("Output winds: ", vmax, "kt")


"""
Code for Binary Search implementaton; to be worked on for later!

#Principle: Regression equation as outlined by the paper. 

#Function to calculate the CKZ pressure; this will be needed for the binary search!
def Pc(V,S,L,P):
  if (latitude <= 18):
    pc = 5.962 - 0.267*V - (V/18.26)**2 - 6.8*S + P
    #Case 1, we typically reduce the importance of latitude in the formula...
  else:
    pc = 23.286 - 0.483*V - (V/24.254)**2 - 12.587*S - 0.483*L + P
    #Case 2, where latitude plays a much more prominent role.
  return(pc)

def vsrm(vmax):
  vsrm1 = vmax - 1.5 * (storm_movement ** 0.63)
  return vsrm1

#Define the parameters for the binary search...
low = 0
high = 200 
diff = high - low
mid = 0
#Binary search algorithm...
while diff > 0.05:
  mid = (high + low) / 2
  mid = vsrm(mid)
  #Find the assumed pressure value...
  p0 = Pc(mid, S, latitude, envp)
  
  #if assumed value is higher than the actual pressure...
  if poci < p0:
    high = mid
  else: 
    low = mid #If assumed value is lower than the actual pressure...
  #Update the difference in winds.
  diff = high - low

mid = (high + low)/2
#Adjust the wind vmax to be presentable.
"""
