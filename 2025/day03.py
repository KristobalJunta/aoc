# Advent of Code
# Year 2025, day 3

import fileinput


def get_input():
    data = list(filter(None, (s.removesuffix("\n") for s in fileinput.input())))
    data = [[int(bat) for bat in bank] for bank in data]
    return data


def bank_max(bank: list[int], num_bat=12):
    values = []
    last_pos = -1

    for i in range(num_bat - 1, -1, -1):
        value = max(bank[last_pos + 1 : len(bank) - i])
        last_pos = bank.index(value, last_pos + 1)
        values.append(value)

    return int("".join(str(v) for v in values))


def part1(data: list[list[int]]):
    return sum(bank_max(bank, 2) for bank in data)


def part2(data: list[list[int]]):
    return sum(bank_max(bank, 12) for bank in data)


if __name__ == "__main__":
    indata = get_input()

    print("--- Part One ---")
    print(part1(indata))

    print("--- Part Two ---")
    print(part2(indata))
