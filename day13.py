arrive, raw_busses = open('data/day13.txt').read().splitlines()
arrive = int(arrive)
busses = [int(x.replace('x', '0')) for x in raw_busses.split(',')]

wait, bus = min((bus - arrive % bus, bus) for bus in busses if bus)
part1 = bus * wait

(_, step), *busses = enumerate(busses)
last, _ = busses[-1]
minutes = step
for offset, bus in busses:
    start = 0
    while offset and bus:
        if (minutes + offset) % bus == 0:
            if start or offset == last:
                step = minutes - start
                break
            else:
                start = minutes
        minutes += step
part2 = minutes

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')