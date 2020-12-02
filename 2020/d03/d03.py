import fileinput
from typing import List
from functools import reduce
import operator


def get_input():
    data = [l.strip() for l in fileinput.input()]
    data = list(filter(bool, data))
    return data


def traverse(data, dr, dc):
    rlen, clen = len(data), len(data[0])
    c = r = 0
    tree_count = 0

    while r < rlen:
        tree_count += int(data[r][c] == '#')
        r += dr
        c = (c + dc) % clen

    return tree_count


def part1(data: List[str]):
    return traverse(data, 1, 3)


def part2(data):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    return reduce(operator.mul, [traverse(data, dr, dc) for dc, dr in slopes], 1)


if __name__ == '__main__':
    indata = get_input()

    res1 = part1(indata)
    res2 = part2(indata)

    print(res1)
    print(res2)
