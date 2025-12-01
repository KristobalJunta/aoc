import fileinput
import re
from collections import defaultdict
from pprint import pprint


def get_input():
    data = [l.strip() for l in fileinput.input()]
    data = list(filter(bool, data))
    return data


def build_tree(data):
    tree = defaultdict(list)
    for line in data:
        line = line.replace('.', '')
        line = re.sub(r'bag(s)?', '', line)
        container, content = line.split(' contain ')
        content = [s.strip() for s in content.split(', ') if not 'no other' in s]
        content = [(int(s[0]), s[2:]) for s in content]
        tree[container.strip()].extend(content)
    tree = dict(tree)
    return tree


def inspect(tree, k, d=0):
    found = d > 0 and 'shiny gold' in k
    totalbags = 0
    for count, color in tree[k]:
        hasgold, numbags = inspect(tree, color, d + 1)
        found = found or hasgold
        totalbags += count * numbags + count
    return found, totalbags


def part1(tree):
    return sum(res for res, _ in (inspect(tree, k) for k in tree))


def part2(tree):
    _, totalbags = inspect(tree, 'shiny gold')
    return totalbags


if __name__ == '__main__':
    indata = get_input()
    tree = build_tree(indata)
    print(part1(tree))
    print(part2(tree))
