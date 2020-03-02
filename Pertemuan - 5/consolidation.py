def main():
    data = [None]
    data = input().split()
    listOfNumber = list(map(int, data))

    numbers = {}
    for number in listOfNumber:
        try:
            numbers[number].append(number)
        except:
            numbers[number] = []
            numbers[number].append(number)

    for val in numbers:
        print(f"{val}: {len(numbers[val])}")

if __name__ == "__main__":
    main()