import re

passports = open('data/day04.txt').read().split('\n\n')


def heightCheck(height: str):
    # (Height) - a number followed by either cm or in:
    if re.search('^\d+(cm|in)$', height):
        (value, unit) = re.match('^(\d+)(\w+)$', height).groups()
        value = int(value)
        # If cm, the number must be at least 150 and at most 193.
        if unit == 'cm':
            if value >= 150 and value <= 193:
                return True
        # If in, the number must be at least 59 and at most 76.
        elif value >= 59 and value <= 76:
            return True
    return False


rules = {
    # (Birth Year) - four digits; at least 1920 and at most 2002.
    'byr': lambda x: int(x) >= 1920 and int(x) <= 2002,
    # (Issue Year) - four digits; at least 2010 and at most 2020.
    'iyr': lambda x: int(x) >= 2010 and int(x) <= 2020,
    # (Expiration Year) - four digits; at least 2020 and at most 2030.
    'eyr': lambda x: int(x) >= 2020 and int(x) <= 2030,
    'hgt': heightCheck,
    # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    'hcl': lambda x: re.search('^#[0-9a-f]{6}$', x),
    # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    # (Passport ID) - a nine-digit number, including leading zeroes.
    'pid': lambda x: re.search('^\d{9}$', x),
    # (Country ID) - ignored, missing or not.
    'cid': lambda x: True,


}


def valid(passport: dict):
    part1, part2 = 1, 1
    for key, rule in rules.items():
        if key not in passport:
            if key != 'cid':
                part1 = 0
                part2 = 0
        elif not rule(passport[key]):
            part2 = 0
    return part1, part2


part1, part2 = 0, 0
for raw in passports:
    pairs = re.split('\s', raw)
    passport = dict(x.split(':') for x in pairs)
    p1, p2 = valid(passport)
    part1 += p1
    part2 += p2

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
