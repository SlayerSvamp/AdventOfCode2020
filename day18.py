from re import sub
questions = open('data/day18.txt').read().splitlines()


def solve_all(pattern):
    def solve(expr):
        while '(' in expr:
            expr = sub(r'\(([^()]+)\)', lambda m: str(solve(m[1])), expr)
        while '+' in expr:
            expr = sub(pattern, lambda m: str(eval(m[0])), expr)
        return eval(expr)

    return sum(map(solve, questions))


print(f'Part 1:', solve_all(r'^\d+ . \d+'))
print(f'Part 2:', solve_all(r'\d+ \+ \d+'))
