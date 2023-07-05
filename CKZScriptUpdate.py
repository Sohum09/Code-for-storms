#Script to calculate the CKZ wind-pressure relationship:
#Reference link: http://www.bom.gov.au/jshess/docs/2009/courtney.pdf

#Taking inputs for each parameter:
vmax = float(input("Enter max winds (in knots): "))
storm_movement = float(input("Enter forward speed (in knots): "))
latitude = float(input("Enter latitude of storm: "))
roci = float(input("Enter ROCI of the storm (in nautical miles): "))
envp = float(input("Enter environmental pressure (in millibars): "))

pc = 0 #The result variable is initialized.

#Velocity of storm with respect to movement speed:
vsrm1 = vmax - 1.5 * (storm_movement ** 0.63)

#S = Storm size factor that is used to adjust the pressure.
S = (roci/60)/8 + 0.1
if(S < 0.4):
  S = 0.4

#From here, we split the formula in two....
if(latitude <= 18):
  #Case 1, we typically reduce the importance of latitude in the formula...
  pc = 5.962 - 0.267 * vsrm1 - (vsrm1 / 18.26) ** 2 - 6.8 * S + envp
else:
  #Case 2, latitude plays a much more important role here...
  pc = 23.286 - 0.483 * vsrm1 - (vsrm1 / 24.254) ** 2 - 12.587 * S - 0.483 * latitude + envp

#We then display the result in an easy to read manner...
pres = "{:.2f}".format(pc+2)
print("CKZ Result: ", int(vmax), "kt,", pres, "mb")

#Special Thanks: Kathy Chan for inputs on ROCI S-ratio, Mckuletzz for the CKZ fix sheet for the ROCI formula.
