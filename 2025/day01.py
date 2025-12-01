# Advent of Code
# Year 2025, day 1

import fileinput


def parseint(s: str):
    return int(s.replace("L", "-").replace("R", "+"))


def get_input():
    data = list(filter(None, (s.removesuffix("\n") for s in fileinput.input())))
    data = [parseint(x) for x in data]
    return data


START_POS = 50


def part1(data):
    pos = START_POS
    zero_clicks = 0

    for step in data:
        pos += step
        pos %= 100

        if pos == 0:
            zero_clicks += 1

    return zero_clicks


def part2(data):
    pos = START_POS
    zero_clicks = 0

    for step in data:
        pos += step

        if pos <= 0 and pos - step != 0:
            zero_clicks += 1

        zero_clicks += abs(pos) // 100
        pos %= 100

    return zero_clicks


if __name__ == "__main__":
    indata = get_input()

    print("--- Part One ---")
    print(part1(indata))

    print("--- Part Two ---")
    print(part2(indata))
