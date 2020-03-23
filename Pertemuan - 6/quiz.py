def main():
    numberOfSizeData = int(input())
    if numberOfSizeData < 1 or numberOfSizeData > 15:
        return

    idMahasiswa = createData(numberOfSizeData, 1, 20)
    if idMahasiswa == False:
        return
        
    nilaiMahasiswa = createData(numberOfSizeData, 1, 100)
    if nilaiMahasiswa == False:
        return

    jumlahMahasiswa = 1
    rataRataNilai = int(nilaiMahasiswa[0])
    tempIdMhs = idMahasiswa[0]
    printData(numberOfSizeData, idMahasiswa, nilaiMahasiswa, tempIdMhs, jumlahMahasiswa, rataRataNilai)

def validation(data, min, max):
    validation = True
    for value in data:
        if int(value) < min or int(value) > max:
            validation = False
            return
    return validation

def createData(numberOfSizeData, min, max):
    data = [None] * numberOfSizeData
    data = input().split()
    if validation(data, min, max) != True:
        return False
    return data

def printData(numberOfSizeData, idMahasiswa, nilaiMahasiswa, tempIdMhs, jumlahMahasiswa, rataRataNilai):
    for i in range(1, numberOfSizeData):
        if tempIdMhs == idMahasiswa[i]:
            jumlahMahasiswa += 1
            rataRataNilai += int(nilaiMahasiswa[i])
        else:
            print(tempIdMhs, rataRataNilai / jumlahMahasiswa, '\n')
            tempIdMhs = idMahasiswa[i]
            jumlahMahasiswa = 1
            rataRataNilai = int(nilaiMahasiswa[i])

    print(tempIdMhs, rataRataNilai / jumlahMahasiswa, '\n')


    



if __name__ == "__main__":
    main()