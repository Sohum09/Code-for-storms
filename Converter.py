with open("For storms.txt", "r") as f:
        data = f.read()
        data = data.split('\n')
        for i in range(len(data)-1):
            row = data[i].split(',')
            if int(row[8]) < 25:
                td_or_db = 'DB'
            elif int(row[8]) < 35:
                td_or_db = 'TD'
            elif int(row[8]) >= 35 and int(row[8]) < 65:
                td_or_db = 'TS'
            else:
                td_or_db = 'HU'
            print(F"{row[2][0:len(row[2])-2]}, {row[2][len(row[2])-2:len(row[2])]}00, , {td_or_db},{row[6][0:len(row[6])-2]}.{row[6][len(row[6])-2:len(row[6])]}, {row[7][0:len(row[7])-2]}.{row[7][len(row[7])-2:len(row[7])]}, {row[8]}, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999,")
