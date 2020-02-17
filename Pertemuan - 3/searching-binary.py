def main():
    listOfNumber = [2,5,8,12,16,23,38,52,76,91]
    findNumber = 100
    i = 0
    h = len(listOfNumber) - 1
    binnarySearch(listOfNumber, findNumber, i, h, 0)

def binnarySearch(listOfNumber, findNumber, i, h, iterasi):
    try:
        midIndex = (i+h) // 2
        if findNumber == listOfNumber[midIndex]:
            print(f'Ditemukan di index ke {midIndex}')
            return
        else:
            if findNumber > listOfNumber[midIndex]:
                i += 1
            elif findNumber < listOfNumber[midIndex]:
                h -= 1
            iterasi += 1    
            binnarySearch(listOfNumber, findNumber, i, h, iterasi)
    except:
        print('Tidak ditemukan')

if __name__ == "__main__":
    main()