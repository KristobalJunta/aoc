import fileinput
import itertools
from functools import reduce


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    return data


def pri(c: str):
    return ord(c) - ord('A') + 27 if c.isupper() else ord(c) - ord('a') + 1


def part1(data):
    def split(s):
        i = int(len(s) / 2)
        return s[:i], s[i:]

    return sum(
        pri(c)
        for comp1, comp2 in [split(s) for s in data]
        for c in (set(comp1) & set(comp2))
    )


def part2(data):
    def grouper(n, iterable):
        args = [iter(iterable)] * n
        return itertools.zip_longest(*args)

    return sum(
        pri(c)
        for group in grouper(3, data)
        for c in reduce(lambda acc, val: acc & set(val), group, set(group[0]))
    )


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
