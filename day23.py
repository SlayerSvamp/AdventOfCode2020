from common import timeit
data = '916438275'  # my input
data = list(map(int, data))


@timeit()
def run(data, moves):
    cup = data[0]
    clockwise = {key: value for key, value in zip(data, data[1:] + data[:1])}
    highest = max(clockwise)

    for _ in range(moves):
        start = clockwise[cup]
        middle = clockwise[start]
        end = clockwise[middle]
        clockwise[cup] = clockwise[end]

        before = cup - 1
        while before in {0, start, middle, end}:
            if not before:
                before = highest
            else:
                before -= 1

        clockwise[end] = clockwise[before]
        clockwise[before] = start
        cup = clockwise[cup]

    return clockwise


clockwise = run(data, 100)
part1 = ''
cup = clockwise[1]
while cup != 1:
    part1 += str(cup)
    cup = clockwise[cup]
print(f'Part 1: {part1}')

data += range(max(data) + 1, 1000_000 + 1)
clockwise = run(data, 10_000_000)
cup = clockwise[1]
print(f'Part 2: {cup * clockwise[cup]}')
