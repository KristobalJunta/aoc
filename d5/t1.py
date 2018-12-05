from collections import Counter


def react(p, units):
    for unit in units:
        p = p.replace(unit+unit.upper(), '').replace(unit.upper()+unit, '')
    return p


with open('input.txt') as infile:
    polymer = infile.read().strip()


print(polymer)

units = dict(Counter(polymer.lower())).keys()

while True:
    new_polymer = react(polymer, units)
    if new_polymer != polymer:
        polymer = new_polymer
    else:
        break

print(polymer)
print(len(polymer))
