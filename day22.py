from common import timeit
import marshal
data = open('data/day22.txt').read().split('\n\n')


def run(func):
    @timeit(func.__name__)
    def wrapper(data):
        decks = list(map(str.splitlines, data))
        decks = [list(map(int, deck[1:])) for deck in decks]
        func(decks)
        combined = decks[0] + decks[1]
        return sum((i+1)*card for i, card in enumerate(combined[::-1]))
    return wrapper


@run
def combat(decks):
    while all(decks):
        p1 = decks[0].pop(0)
        p2 = decks[1].pop(0)
        winner = p1 < p2
        decks[winner] += [[p1, p2], [p2, p1]][winner]


@run
def recursive_combat(decks):
    def inner(decks):
        states = set()
        while all(decks):
            state = marshal.dumps(decks)
            if state in states:
                return 0
            states.add(state)

            p1 = decks[0].pop(0)
            p2 = decks[1].pop(0)
            if p1 <= len(decks[0]) and p2 <= len(decks[1]):
                winner = inner([decks[0][:p1], decks[1][:p2]])
            else:
                winner = p1 < p2
            decks[winner] += [[p1, p2], [p2, p1]][winner]
        return winner
    inner(decks)


print(f'Part 1: {combat(data)}')
print(f'Part 2: {recursive_combat(data)}')
