import re

instructions = open('data/day14.txt').read().splitlines()


def floating(mask):
    if 'X' not in mask:
        yield int(mask, 2)
        return
    for i in [0, 1]:
        new = re.sub('X', f'{i}', mask, 1)
        yield from floating(new)


mem = {}
mem2 = {}

for ins in instructions:
    if ins.startswith('mask'):
        mask = ins.replace('mask = ', '')
        and_1 = int(mask.replace('X', '1'), 2)
        or_1 = int(mask.replace('X', '0'), 2)
        and_2 = int(mask.replace('0', '1').replace('X', '0'), 2)
        masks = list(floating(mask))
        continue

    address, value = [int(x) for x in re.findall(r'(\d+)', ins)]

    mem[address] = value & and_1 | or_1

    for or_2 in masks:
        mem2[address & and_2 | or_2] = value


part1 = sum(mem.values())
part2 = sum(mem2.values())

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')