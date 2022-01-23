from data import *

def buatTabel(data):
  print('\n\t_______________________________________________________________________________________________________\n')
  print('\t No', end='\t')
  for key in data[0]:
      print('|', key, end='\t')
  print('\n\t_______________________________________________________________________________________________________\n')

  for i in range(len(data)):
      print('\t', (i+1), end='')
      for key in data[i]:
          print('\t|', data[i][key], end='')
      print()
  print('\n\t_______________________________________________________________________________________________________\n')

def tigaTerlaris(data):
  no1 = 0
  no2 = 0
  no3 = 0
  for key in data:
    if no1 < data.get(key):
      no1 = data.get(key)

  for key in data:
    if no2 < data.get(key) and data.get(key) < no1:
      no2 = data.get(key)

  for key in data:
    if no3 < data.get(key) and data.get(key) < no2:
      no3 = data.get(key)

  return {
    list(data.keys())[list(data.values()).index(no1)]: no1,
    list(data.keys())[list(data.values()).index(no2)]: no2,
    list(data.keys())[list(data.values()).index(no3)]: no3
  }

def semuaBulanTerlaris():
  for i in range(len(dataPenjualan)):
    print(i + 1, tigaTerlaris(dataPenjualan[i]))

semuaBulanTerlaris()