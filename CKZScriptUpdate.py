#Script to calculate the CKZ wind-pressure relationship:
#Reference link: http://www.bom.gov.au/jshess/docs/2009/courtney.pdf

import numpy as np

#Taking inputs for each parameter:
vmax = float(input("Enter max winds (in knots): "))
storm_movement = float(input("Enter forward speed (in knots): "))
latitude = float(input("Enter latitude of storm: "))

Ask = input("Is R34 known? 'yes' or 'no'. ")
if Ask=='yes':
  R34NE = float(input("Enter gale radius at the NE quadrant (nm): "))
  R34SE = float(input("Enter gale radius at the SE quadrant (nm): "))
  R34SW = float(input("Enter gale radius at the SW quadrant (nm): "))
  R34NW = float(input("Enter gale radius at the NW quadrant (nm): "))
elif Ask=='no':
  pass
  
roci = float(input("Enter ROCI of the storm (in nm): "))
envp = float(input("Enter environmental pressure (in mb/hPa): "))

#Velocity of storm with respect to movement speed:
vsrm1 = vmax - 1.5 * (storm_movement ** 0.63)

#S = Storm size factor that is used to adjust the pressure.

#1.ROCI
S_ROCI = (roci/60)/8 + 0.1
if(S_ROCI < 0.4):
  S_ROCI = 0.4
  
#2.R34
R34 = np.array([R34NE, R34SE, R34SW, R34NW])
AVGR34 = np.mean(R34)
V500 = AVGR34/9 -3
V500c = vmax*(((66.785 - 0.09102*vmax + 1.0619*(latitude-25))/500)**(0.1147 + 0.0055*vmax-0.001*(latitude-25)))
S_R34 = V500/V500c
if (S_R34 < 0.4):
  S_R34 = 0.4

#From here, we split the formula in two....
def Pc(V,S,L,P):
  if (latitude <= 18):
    pc = 5.962 - 0.267*V - (V/18.26)**2 - 6.8*S + P
  #Case 1, we typically reduce the importance of latitude in the formula...
  else:
    pc = 23.286 - 0.483*V - (V/24.254)**2 - 12.587*S - 0.483*L + P
  return(pc)

#We then display the result in an easy to read manner...
if Ask == 'no':
  pass
elif Ask == 'yes':
  Pc_R34 = round(Pc(vsrm1,S_R34,latitude,envp), 2)
  print ("CKZ Result (R34): ", int(vmax), "kt,", Pc_R34, "mb")
Pc_ROCI = round(Pc(vsrm1,S_ROCI,latitude,envp), 2)

print ("CKZ Result (ROCI): ", int(vmax), "kt,", Pc_ROCI, "mb")
#Special Thanks: Kathy Chan for inputs on revising the code, Mckuletzz for the CKZ fix sheet for the ROCI formula for S-ratio.
