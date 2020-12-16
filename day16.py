import re
raw_fields, raw_tickets = open('data/day16.txt').read().split('\n\n', 1)

field_range = {}
valid = set()
for line in raw_fields.splitlines():
    field, _ = line.split(': ')
    from1, to1, from2, to2 = map(int, re.findall(r'\d+', line))
    field_range[field] = set([*range(from1, to1 + 1), *range(from2, to2 + 1)])
    valid.update(field_range[field])

tickets = []
part1 = 0
for line in raw_tickets.splitlines():
    if ',' in line:
        ticket = [*map(int, line.split(','))]
        invalid = [x for x in ticket if x not in valid]
        part1 += sum(invalid)
        if not invalid:
            tickets.append(ticket)

possible = {i: set(field_range) for i in range(len(field_range))}
for ticket in tickets:
    for i, fields in [*possible.items()]:
        for field in [*fields]:
            if ticket[i] not in field_range[field]:
                possible[i].remove(field)

part2 = 1
ignore = set()
for i, fields in sorted(possible.items(), key=lambda x: len(x[1])):
    if len(fields - ignore) == 1:
        field, = fields - ignore
        if 'departure' in field:
            part2 *= tickets[0][i]
        ignore.add(field)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
