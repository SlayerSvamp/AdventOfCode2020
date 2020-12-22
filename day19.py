from time import perf_counter

raw = open('data/day19.txt').read().split('\n\n')
raw_rules, data = map(str.splitlines, raw)
start = perf_counter()


rules = {}
for rule in raw_rules:
    key, value = rule.split(': ')
    if '"' in value:
        rules[int(key)] = value[1:-1]
    else:
        rule = []
        for value in value.split(' | '):
            rule.append([*map(int, value.split(' '))])
        rules[int(key)] = rule


def match(rules, message):
    def inner(key, parent):
        if type(rules[key]) is str:
            yield rules[key]
            return
        for sub_rule in rules[key]:
            accumulated = ['']
            for rule in sub_rule:
                temp = []
                for acc in accumulated:
                    for ret in inner(rule, parent + acc):
                        if parent + acc + ret in message:
                            temp.append(acc+ret)
                accumulated = temp
            yield from accumulated

    return message in inner(0, '')


part1 = sum(match(rules, message) for message in data)
print(f'Par1 done in {perf_counter() - start:.2f} seconds')
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
part2 = sum(match(rules, message) for message in data)
print(f'Par2 done in {perf_counter() - start:.2f} seconds')

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
