import re

lines = open('data/day07.txt').read().splitlines()
# lines = [
#     'light red bags contain 1 bright white bag, 2 muted yellow bags.',
#     'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
#     'bright white bags contain 1 shiny gold bag.',
#     'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
#     'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
#     'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
#     'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
#     'faded blue bags contain no other bags.',
#     'dotted black bags contain no other bags.',
# ]


class Bag:
    bags = {}

    def __init__(self, line):
        values = re.findall(r'(\w+ \w+ bag|\d+)', line)
        self.name, *values = values
        self.parents = set()
        self.inside = set()
        self.children = {}
        if len(values) > 1:
            while values:
                count, child, *values = values
                self.children[child] = int(count)
        Bag.bags[self.name] = self

    def ancestors(self):
        retval = set()
        for parent in self.parents:
            retval.add(parent.name)
            for ancestor in parent.ancestors():
                retval.add(ancestor)
        return retval

    def countInside(self):
        count = 0
        for bag in self.inside:
            count += self.children[bag.name]
            count += self.children[bag.name] * bag.countInside()
        return count

    @staticmethod
    def setup(lines):
        for line in lines:
            Bag(line)

        Bag.setupRelations()

    @staticmethod
    def setupRelations():
        for bag in Bag.bags.values():
            for child in bag.children:
                inside = Bag.bags[child]
                inside.parents.add(bag)
                bag.inside.add(inside)


Bag.setup(lines)


myBag = Bag.bags['shiny gold bag']
part1 = len(myBag.ancestors())
part2 = myBag.countInside()

print('Part 1:', part1)
print('Part 2:', part2)
