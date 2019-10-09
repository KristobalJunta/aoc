from collections import Counter


def react(p, units):
    for unit in units:
        p = p.replace(unit+unit.upper(), '').replace(unit.upper()+unit, '')
    return p


with open('input.txt') as infile:
    polymer = infile.read().strip()


units = dict(Counter(polymer.lower())).keys()
result = dict()
original_polymer = polymer

for unit in units:
    polymer = original_polymer.replace(unit, '').replace(unit.upper(), '')

    while True:
        new_polymer = react(polymer, units)
        if new_polymer != polymer:
            polymer = new_polymer
        else:
            break

    result[unit] = len(polymer)

ans = min(result.items(), key=lambda el: el[1])
print(ans)
