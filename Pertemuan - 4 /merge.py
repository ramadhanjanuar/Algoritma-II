def main():
    mhsA = [
        {
            'nik': 359601,
            'nama': 'Adi Purwanto',
            'nilai': 3.82
        },
        {
            'nik': 359604,
            'nama': 'Fitria Susanti',
            'nilai': 2.97
        },
        {
            'nik': 359605,
            'nama': 'Dewi Ramdhani',
            'nilai': 2.74
        },
        {
            'nik': 359606,
            'nama': 'Adri Yanto',
            'nilai': 3.02
        }
    ]

    mhsB = [
        {
            'nik': 359603,
            'nama': 'Adi Purwanto',
            'nilai': 3.82
        },
        {
            'nik': 359609,
            'nama': 'Fitria Susanti',
            'nilai': 2.97
        },
        {
            'nik': 359614,
            'nama': 'Dewi Ramdhani',
            'nilai': 2.74
        }
    ]

    afterMerge = []

    for value in mhsA:
        afterMerge.append(value)
    
    for value in mhsB:
        afterMerge.append(value)

    print(afterMerge)

    for value in afterMerge:
        print(f'NIK: {value["nik"]}')
        print(f'Nama: {value["nama"]}')
        print(f'Nilai: {value["nilai"]}')
        print('\n')

if __name__ == "__main__":
    main()