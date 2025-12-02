# Advent of Code
# Year 2025, day 2

import fileinput
from itertools import batched


def get_input():
    data = list(filter(None, (s.removesuffix("\n") for s in fileinput.input())))

    def parse_range(r):
        return tuple(map(int, r.split("-")))

    ranges = list(map(parse_range, data[0].split(",")))
    return ranges


def split(s, n):
    len_ = len(s)

    if len_ % n:
        raise ValueError

    chunk = len_ // n
    parts = list(batched(s, chunk))
    return parts


def part1(ranges):
    def not_valid(num):
        try:
            parts = split(str(num), 2)
        except ValueError:
            return False
        else:
            return len(set(parts)) == 1

    total = sum(
        num
        for start, end in ranges
        for num in range(start, end + 1)
        if not_valid(num)
    )

    return total


def part2(ranges):
    def not_valid(num):
        s = str(num)
        for n in range(2, len(s) + 1):
            try:
                parts = split(s, n)
            except ValueError:
                pass
            else:
                if len(set(parts)) == 1:
                    return True
        return False

    total = sum(
        num
        for start, end in ranges
        for num in range(start, end + 1)
        if not_valid(num)
    )

    return total


if __name__ == "__main__":
    indata = get_input()

    print("--- Part One ---")
    print(part1(indata))

    print("--- Part Two ---")
    print(part2(indata))
