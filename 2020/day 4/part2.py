import re
import sys

HCL_REGEX = re.compile('#[a-f|0-9]{6}')
PID_REGEX = re.compile('[0-9]{9}')


def validate_byr(value):
    return 1920 <= int(value) <= 2002


def validate_iyr(value):
    return 2010 <= int(value) <= 2020


def validate_eyr(value):
    return 2020 <= int(value) <= 2030


def validate_hgt(value):
    if value.endswith('cm'):
        return 150 <= int(value.replace('cm', '')) <= 193
    elif value.endswith('in'):
        return 59 <= int(value.replace('in', '')) <= 76
    else:
        return False


def validate_hcl(value):
    return bool(HCL_REGEX.fullmatch(value))


def validate_ecl(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(value):
    return bool(PID_REGEX.fullmatch(value))


if __name__ == '__main__':
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    validator = {
        'byr': validate_byr,
        'iyr': validate_iyr,
        'eyr': validate_eyr,
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': validate_pid,
    }

    count = 0
    passport = {}

    for line in sys.stdin:
        if len(line.replace('\n', '')) == 0:
            if len(passport) == len(required):
                print(passport)
                count += 1
            passport = {}
        for field in line.replace('\n', '').split(' '):
            components = field.split(':')
            if components[0] in required and validator[components[0]](components[1]):
                passport[components[0]] = components[1]

    print(count)
