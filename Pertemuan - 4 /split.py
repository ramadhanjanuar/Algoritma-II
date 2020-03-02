def main():
    data = [
        {
            'nip': '001',
            'gol': 'B'
        },
        {
            'nip': '030',
            'gol': 'B'
        },
        {
            'nip': '057',
            'gol': 'C'
        },
        {
            'nip': '095',
            'gol': 'A'
        },
        {
            'nip': '102',
            'gol': 'B'
        },
        {
            'nip': '135',
            'gol': 'C'
        }
    ]   

    nipUnder100 = []
    nipAbove100 = []

    for value in data:
        if int(value['nip']) < 100:
            nipUnder100.append(value)
        else:
            nipAbove100.append(value)
    
    print('#tugas SPLIT NIP dibawah dan diatas 100')
    print('NIP diatas 100')
    print(nipAbove100)
    print('NIP dibawah 100')
    print(nipUnder100)

if __name__ == "__main__":
    main()