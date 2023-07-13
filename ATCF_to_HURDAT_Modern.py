#This code was created by Kathy Chan. Credits to her!

NAME = "DINGANI" #Enter name of the storm that you want to input
YEAR = 2023 #Enter year that the storm takes place in.

data_tc = pd.read_csv("202313S_Dingani_Track.txt", usecols=range(11), header=None)
col_names = data_tc.columns
data_tc.columns =['Hem', '#', 'Dt', '.', 'Best', 'O', 'Lat', 'Lon', 'Wind', 'Pressure', 'status']
n = data_tc.shape[0]
intensity = data_tc['Wind']
pressure = data_tc['Pressure']
time = data_tc['Dt']
i=1
while i < n:
  if time[i-1]==time[i]:
    data_tc=data_tc.drop(labels=i, axis=0)
    i=i+1
  else:
    i=i+1
data_tc2 = data_tc.copy()
m = data_tc2.shape[0]
D=100
data_tc2['date'] = time//D
data_tc2['time'] = time%D*100
data_tc2['time'] = data_tc2['time'].astype('string')
data_tc2['time'] = data_tc2['time'].apply(lambda x: '{:0>4}'.format(x))
data_tc2 = data_tc2.drop(['Dt', '.'], axis=1)
data_tc2['Lat']=data_tc2['Lat'].str.replace(r'\w{2}(?!$)', r'\g<0>.', regex=True)
data_tc2['Lon']=data_tc2['Lon'].str.replace(r'\w{2}(?!$)', r'\g<0>.', regex=True)
print(F"{data_tc2['Hem'].iloc[-1]}{data_tc2['#'].iloc[-1]}{YEAR}, {NAME:>18}, {m:5},")
for j in range(m):
  HURDAT = F"{data_tc2['date'].iloc[j]}, {data_tc2['time'].iloc[j]},  ,{data_tc2['status'].iloc[j]},{data_tc2['Lat'].iloc[j]:5},{data_tc2['Lon'].iloc[j]:5}, {data_tc2['Wind'].iloc[j]:3}, {data_tc2['Pressure'].iloc[j]:4}, {0:4}, {0:4}, {0:4}, {0:4}, {0:4}, {0:4}, {0:4}, {0:4}, {0:4}, {0:4}, {0:4}, {0:4},"
  print(HURDAT)
