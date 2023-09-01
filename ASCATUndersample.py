#Quick script that calculates the actual aggressed windspeed from the recorded ASCAT windspeed, as highlighted in Chou et al. 2013
#Input parameter:
AWS = float(input("Enter the ASCAT vmax recorded in kt: "))
DWS = 0 #Approx value for true winds, denoted as Dropsonde Wind Speed.

#The formula works in m/s values, so we will first convert AWS to m/s:
AWS = AWS / 1.94384

#Applying the regression formula created by Chou et. al 2013:
DWS = (0.014 * AWS ** 2) + (0.821 * AWS) + 0.961

#We will now convert the m/s output to kts:
DWS = DWS * 1.94384

#Present the output in a readable manner:
DWS = "{:.2f}".format(DWS)
print("The adjusted representative windspeed: ", DWS, "kt")
