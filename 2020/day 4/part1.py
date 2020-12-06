import sys

if __name__ == '__main__':
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    count = 0
    passport = {}

    for line in sys.stdin:
        if len(line.replace('\n', '')) == 0:
            if len(passport) == len(required):
                count += 1
            passport = {}
        for field in line.replace('\n', '').split(' '):
            components = field.split(':')
            if components[0] in required:
                passport[components[0]] = None

    print(count)
