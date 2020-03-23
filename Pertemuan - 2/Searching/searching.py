def main():
    numberOfSizeData = int(input())
    data = [None] * numberOfSizeData
    data = input().split()

    numberOfSizeDataSearching = int(input())
    dataSearching = [None] * numberOfSizeDataSearching
    dataSearching = input().split()

    notFound = False
    for indexDataSearching, valueDataSearching in enumerate(dataSearching):
        if(notFound and indexDataSearching != 0):
            print('Tidak ditemukan')
        for valueData in data:
            if int(valueDataSearching) == int(valueData):
                print(f'Ditemukan di index ke {indexDataSearching}')
                notFound = False
                break
            else:
                notFound = True
        if(notFound and indexDataSearching == len(dataSearching)-1):
            print('Tidak ditemukan')

if __name__ == "__main__":
    main()