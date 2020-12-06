import sys

if __name__ == '__main__':
    cases = [
        {
            'count': 0,
            'right': 1,
            'down': 1,
        },
        {
            'count': 0,
            'right': 3,
            'down': 1,
        },
        {
            'count': 0,
            'right': 5,
            'down': 1,
        },
        {
            'count': 0,
            'right': 7,
            'down': 1,
        },
        {
            'count': 0,
            'right': 1,
            'down': 2,
        },
    ]

    idx = 0

    for line in sys.stdin:
        for case in cases:
            if idx % case['down'] == 0:
                x = int(idx * case['right'] / case['down']) % (len(line) - 1)
                if line[x] == '#':
                    case['count'] = case['count'] + 1
        idx += 1

    result = 1
    for case in cases:
        result = result * case['count']

    print(result)
