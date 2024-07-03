
name = input().upper()
yr = input()
month = input().zfill(2)
day = input().zfill(2)
hour = input().zfill(2)
enhancement = input() 
if enhancement == 'BD' or enhancement == 'NHC':
    enhancement = enhancement.lower()
elif enhancement == 'ir1-ir2' or enhancement == 'ir4-ir1':
    enhancement = enhancement.upper()
else:
    enhancement = enhancement.upper()
satellite = input().upper()

satelliteMap = {'GMS1':'GMS1', 'GMS2':'GMS2', 'GMS3':'GMS3', 'GMS4':'GMS4', 'GMS5':'GMS5', 'GOE9':'GOE9', 'MTS1':'MTS1', 'MTS2':'MTS2', 'HMW8':'HMW8', 'HMW9':'HMW9'}
enhancementMap = {'VIS':'0', 'IR1':'1', 'IR2':'2', 'IR3': '3', 'IR4': '4', 'BD': 'bd', 'bd': 'bd', 'nhc': 'nhc', 'IR1-IR2': 'IR1-IR2', 'IR4-IR1': 'IR4-IR1'}

if(name == 'NOT_NAMED'):
    print("Due to the IBTRACS database being ambiguous with this name, it cannot be used.")
jma = ""
with open("bst_all.txt", "r") as file:
    data = file.read()
    data = data.split('\n')
    for i in range(len(data)-1):
        row = data[i].split()
        
        if row[0] == '66666':
            
            if len(row) == 7:
                continue
            if (row[7] == name or row[6] == name) and yr[2:] == row[1][:2]:
                print(row)
                print(len(row))
                jma += yr + row[1][2:]
                break
print(jma)

url = f"http://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/{jma}/{enhancementMap[enhancement]}/512x512/{satelliteMap[satellite]}{yr[2:]}{month}{day}{hour}.{jma}.jpg"
print(url)