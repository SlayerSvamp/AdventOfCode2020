import re
lines = open('data/day21.txt').read().splitlines()
pattern = r'(.*) \(contains (.*)\)'
allergens = {}
all_ingredients = []

# populate with possible items
for line in lines:
    ingredients, raw_allergens = re.match(pattern, line).groups()
    ingredients = ingredients.split(' ')
    all_ingredients += ingredients
    for allergen in raw_allergens.split(', '):
        allergens.setdefault(allergen, set(ingredients))
        allergens[allergen] &= set(ingredients)

# clean up
left = set(allergens)
while left:
    for allergen, ingredients in allergens.items():
        if len(ingredients) == 1:
            left.discard(allergen)
            for x in left:
                allergens[x] -= ingredients

# resolve
allergens = {key: value for key, (value,) in allergens.items()}
part1 = sum(x not in allergens.values() for x in all_ingredients)
part2 = ','.join([value for _, value in sorted(allergens.items())])

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
