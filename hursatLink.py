import csv

#Initialize the script by creating the inquiry....
btkID = input("Enter the Storm ID: ")
yr = input("Enter year: ")

btkID = btkID.upper()
#Load in the loops for finding the latitude and longitude...
IBTRACS_ID = f"{btkID}{yr}"
hursat_ID = ""
with open('ibtracs.ALL.list.v04r00.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for line_num, lines in enumerate(csvFile, start=1):
        if line_num > 3:
            #Process or print the lines from the 4th line onwards
                #If IBTRACS ID matches the ID on the script...
                if lines[18] == IBTRACS_ID or (btkID == lines[5] and yr == lines[6][:4]):
                    hursat_ID = lines[0]
                    break

url = f"https://www1.ncdc.noaa.gov/pub/data/satellite/hursat/{yr}/{hursat_ID}/"
print(url)
