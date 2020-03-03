data = input().split()
listOfNumber = list(map(int, data))

key = listOfNumber[0]
num = 0
for number in listOfNumber:
    if key == number:
        num += 1
    else:
        print(f'{key}: {num}')
        key = number
        num = 1
print(f'{key}: {num}')

