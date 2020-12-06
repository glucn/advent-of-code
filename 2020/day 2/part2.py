import sys


def parse_line(text: str) -> (int, int, str, str):
    components = text.split(' ')
    numbers = components[0].split('-')
    return int(numbers[0]), int(numbers[1]), components[1].split(':')[0], components[2]


def is_char(text: str, idx: int, cha: str) -> bool:
    if len(text) < idx:
        return False
    return text[idx:idx+1] == cha


if __name__ == '__main__':
    count = 0

    for line in sys.stdin:
        position1, position2, char, password = parse_line(line)
        if is_char(password, position1 - 1, char) != is_char(password, position2 - 1, char):
            count += 1

    print(count)
