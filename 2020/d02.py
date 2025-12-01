import itertools
import fileinput
from collections import Counter
from typing import List
from functools import reduce


def get_input():
    data = [l for l in fileinput.input()]
    return data


def parse_str(line):
    policy, letter, pwd = line.split()
    letter = letter[0]
    pol_min, pol_max = [int(i) for i in policy.split('-')]
    return pol_min, pol_max, letter, pwd


def part1(data: List[str]):
    def is_valid(line):
        pol_min, pol_max, letter, pwd = parse_str(line)
        letter_count = Counter(pwd)
        is_valid = pol_min <= letter_count.get(letter, -1) <= pol_max
        return int(is_valid)

    return sum(is_valid(s) for s in data)


def part2(data):
    def is_valid(line):
        pol_min, pol_max, letter, pwd = parse_str(line)
        pwd = " " + pwd
        is_valid = (letter == pwd[pol_min]) ^ (letter == pwd[pol_max])
        return int(is_valid)

    return sum(is_valid(s) for s in data)


if __name__ == '__main__':
    indata = get_input()

    res1 = part1(indata)
    res2 = part2(indata)

    print(res1)
    print(res2)
