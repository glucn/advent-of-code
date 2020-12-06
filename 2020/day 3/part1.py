import sys

if __name__ == '__main__':
    count = 0

    right = 3
    x = 0

    for line in sys.stdin:
        if line[x] == '#':
            count += 1
        x = (x + right) % (len(line)-1)

    print(count)
