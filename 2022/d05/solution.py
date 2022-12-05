import fileinput
import numpy as np
from copy import copy


def parse_stacks(stacks):
    # make sure all stacks are equal length
    maxl = max(len(s) for s in stacks)
    stacks = [s.ljust(maxl, ' ') for s in stacks]

    stacks = np.array([list(s) for s in stacks]).T
    stacks = stacks[1::4]
    stacks = [list(s)[::-1][1:] for s in stacks]
    stacks = [''.join(s).strip() for s in stacks]
    stacks.insert(0, None)

    return stacks


def parse_commands(commands):
    return [list(map(int, c.split()[1::2])) for c in commands]


def get_input():
    data = [s.removesuffix('\n') for s in fileinput.input()]
    data = list(filter(bool, data))

    stacks, commands = [], []

    for line in data:
        if line.startswith("move"):
            commands.append(line)
        else:
            stacks.append(line)

    stacks = parse_stacks(stacks)
    commands = parse_commands(commands)

    return stacks, commands


def part1(stacks, commands):
    stacks = copy(stacks)

    for count, from_, to in commands:
        stacks[to] = stacks[to] + stacks[from_][-count:][::-1]
        stacks[from_] = stacks[from_][:-count]

    return ''.join(s[-1] for s in stacks[1:])


def part2(stacks, commands):
    stacks = copy(stacks)

    for count, from_, to in commands:
        stacks[to] = stacks[to] + stacks[from_][-count:]
        stacks[from_] = stacks[from_][:-count]

    return ''.join(s[-1] for s in stacks[1:])


if __name__ == '__main__':
    stacks, commands = get_input()
    print(part1(stacks, commands))
    print(part2(stacks, commands))
