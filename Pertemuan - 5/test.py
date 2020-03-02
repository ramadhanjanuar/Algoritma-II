f = open("mhs.txt", "r")
dataMhs = []
mahasiswa = {}
for x in f:
  a = x.replace('\n','').split(' ')
  
  try :
      mhs = {
          'matkul': a[1],
          'nilai': a[2]
      }
      mahasiswa[a[0]].append(mhs)
  except:
    mahasiswa[a[0]]= []
    mhs = {
          'matkul': a[1],
          'nilai': a[2]
      }
    mahasiswa[a[0]].append(mhs)
    
matkuliah = []

for npm in mahasiswa:
  for matkul in mahasiswa[npm]:
    if matkul['matkul'] not in matkuliah:
      matkuliah.append(matkul['matkul'])

print(f'jumlah matkul: {len(matkuliah)}')
for mhs in mahasiswa:
  print(f"NPM {mhs} memiliki {len(mahasiswa[mhs])} matkul")
  
