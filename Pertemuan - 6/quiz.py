def main():
    numberOfSizeData = int(input())
    if numberOfSizeData < 1 or numberOfSizeData > 15:
        return

    idMahasiswa = [None] * numberOfSizeData
    idMahasiswa = input().split()
    if validation(idMahasiswa, 1, 20) != True:
        return
        
    nilaiMahasiswa = [None] * numberOfSizeData
    nilaiMahasiswa = input().split()
    if validation(nilaiMahasiswa, 1, 100) != True:
        return

    jumlahMahasiswa = 1
    rataRataNilai = int(nilaiMahasiswa[0])
    tempIdMhs = idMahasiswa[0]

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
    

    

def validation(data, min, max):
    validation = True
    for value in data:
        if int(value) < min or int(value) > max:
            validation = False
            return False
    return validation


    



if __name__ == "__main__":
    main()