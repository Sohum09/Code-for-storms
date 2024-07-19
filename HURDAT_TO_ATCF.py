#20130815, 0000,  , DB,  7.6N, 167.3W,  25, 1009,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, -999

#WP, 28, 2013101906,   , BEST,   0,  92N, 1633E,  15, 1010, DB,   0,    ,    0,    0,    0,    0, 

with open('hurdat2.txt', mode='r') as file:
    lines = (file.read()).split("\n")
    for line in lines:
        hurdat2 = line.split(',')
        atcfLine = f"CP, 01, {hurdat2[0]}{hurdat2[1][:3].strip()},   , BEST,   0,  {int(float(hurdat2[4][:-1].strip())*10)}{hurdat2[4][-1].strip()}, {int(float(hurdat2[5][:-1].strip())*10)}{hurdat2[5][-1].strip()},  {hurdat2[6].strip()}, {hurdat2[7].strip()}, {hurdat2[3].strip()},   0,    ,    0,    0,    0,    0,"
        print(atcfLine)