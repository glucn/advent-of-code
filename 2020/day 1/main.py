import sys

if __name__ == '__main__':
    numbers = {}

    for line in sys.stdin:
        number = int(line)
        if (2020 - number) in numbers:
            print(number * (2020 - number))
        numbers[number] = None
