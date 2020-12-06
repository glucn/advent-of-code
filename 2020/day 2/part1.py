import sys


def parse_line(text: str) -> (int, int, str, str):
    components = text.split(' ')
    numbers = components[0].split('-')
    return int(numbers[0]), int(numbers[1]), components[1].split(':')[0], components[2]


if __name__ == '__main__':
    count = 0

    for line in sys.stdin:
        min_policy, max_policy, char, password = parse_line(line)
        occurrences = password.count(char)
        if min_policy <= occurrences <= max_policy:
            count += 1

    print(count)
