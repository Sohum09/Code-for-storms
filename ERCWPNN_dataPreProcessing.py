import csv
import statistics
import math

nameList = []

# First, read and process the ERCStormList.csv file
with open('ERCStormList.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for line_num, lines in enumerate(csvFile, start=1):
        if line_num > 1:
            stormNames = []
            stormNames.append(lines[1].upper())
            stormNames.append(lines[2])
            nameList.append(stormNames)

fields = ['name', 'year', 'pressure', 'r34avg', 'roci', 'envp', 'outerEW', 'innerEW', 'momentumRatio', 'coriolis', 'winds']
parentRow = []

# Now, read and process the ibtracs.ALL.list.v04r01.csv file
k=0
while k < len(nameList):
    with open('ibtracs.ALL.list.v04r01.csv', mode='r') as file:
        csvFile = csv.reader(file)
        for line_num, lines in enumerate(csvFile, start=1):
            if line_num > 3:
                if nameList[k][0] == lines[5] and nameList[k][1] == lines[6][:4]:
                    winds = lines[23].strip()
                    status = lines[22].strip()

                    # Skip certain statuses or empty winds
                    if status in ['DB', 'WV', 'LO', 'MD', 'EX'] or not winds:
                        continue
                    
                    winds = float(winds)
                    if winds >= 64:
                        try:
                            pressure = float(lines[24].strip())
                            r34avg = statistics.mean([
                                float(lines[26].strip()), 
                                float(lines[27].strip()), 
                                float(lines[28].strip()), 
                                float(lines[29].strip())
                            ])
                            roci = float(lines[39].strip())
                            envp = float(lines[38].strip()) + 1

                            innerEW = lines[40].strip()
                            if not innerEW:
                                continue  # Skip row if innerEW is empty
                            innerEW = float(innerEW)

                            momentumRatio = float('inf') if roci == 0 else innerEW / roci
                            coriolis = 2 * (7.292 * 10**(-5)) * math.sin(-1 * float(lines[19].strip()))

                            row = [nameList[k][0], nameList[k][1], pressure, r34avg, roci, envp, '', innerEW, momentumRatio, coriolis, winds]
                            parentRow.append(row)
                            print(row)
                        except ValueError:
                            continue  # Skip row if any conversion fails
    k += 1  # Move to the next storm in nameList


# Finally, write the results to a new CSV file
filename = "parentDatasetFirstPass.csv"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(parentRow)
