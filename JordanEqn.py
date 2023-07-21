#Script to convert the Jordan Equation into derived sfc pressure.
#Reference Link: https://www.researchgate.net/publication/249612725_Supertyphoon_Forrest_September_1983_The_Overlooked_Record_Holder_of_Intensification_in_24_36_and_48_h

#Input
height = float(input("Enter the observed 700mb Height (in m): "))
Pc = 0


Pc = 645 + 0.115 * height
Pc = "{:.2f}".format(Pc)

print("The extrapolated pressure:", Pc, "mb")
