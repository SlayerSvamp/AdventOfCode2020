groups = [group.splitlines() for group in open(
    'data/day06.txt').read().split('\n\n')]

part1 = 0
part2 = 0
for group in groups:
    part1 += len(set(''.join(group)))
    for ans in group[0]:
        if not sum(1 for x in group if ans not in x):
            part2 += 1


print(f'Part 1: {part1}')
print(f'Part 1: {part2}')
