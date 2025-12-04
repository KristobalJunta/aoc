# Advent of Code
# Year Y, day X

import copy
import itertools
import fileinput


def get_input():
    data = list(filter(None, (s.removesuffix("\n") for s in fileinput.input())))
    data = [list(x) for x in data]
    return data


def find_accessible(mx: list[list[str]]):
    x_max = len(mx)
    y_max = len(mx[0])

    to_remove = list()

    for i in range(x_max):
        for j in range(y_max):
            if mx[i][j] != "@":
                continue

            neighb_count = 0

            for dx, dy in itertools.product([1, -1, 0], repeat=2):
                if dx == 0 and dy == 0:
                    continue

                if i + dx < 0 or i + dx >= x_max or j + dy < 0 or j + dy >= y_max:
                    continue

                if mx[i + dx][j + dy] == "@":
                    neighb_count += 1

            if neighb_count < 4:
                to_remove.append((i, j))

    return to_remove


def part1(mx):
    accessible_rolls = find_accessible(mx)
    return len(accessible_rolls)


def part2(data):
    mx = copy.deepcopy(data)
    total_removed = 0

    while True:
        accessible_rolls = find_accessible(mx)

        if len(accessible_rolls) == 0:
            break

        for x, y in accessible_rolls:
            mx[x][y] = "."

        total_removed += len(accessible_rolls)

    return total_removed


if __name__ == "__main__":
    indata = get_input()

    print("--- Part One ---")
    print(part1(indata))

    print("--- Part Two ---")
    print(part2(indata))
