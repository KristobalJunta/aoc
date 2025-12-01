import fileinput
from copy import deepcopy
import itertools


def get_input():
    data = [list(l.strip()) for l in fileinput.input()]
    data = list(filter(bool, data))
    return data


def debug(state):
    print('\n'.join([''.join(r) for r in state]))


def evolve(state, maxdist=1, tolerance=4):
    changed = False
    new_state = deepcopy(state)

    rowc = len(state)
    colc = len(state[0])

    maxdist = min(max(rowc, colc), maxdist) + 1

    for r in range(rowc):
        for c in range(colc):
            occupied = 0
            seat = state[r][c]
            if seat == '.':
                continue
            for dr, dc in itertools.product([0, -1, 1], repeat=2):
                if dr == dc == 0:
                    continue
                for dist in range(1, maxdist):
                    nr = r + dr * dist
                    nc = c + dc * dist
                    if nr < 0 or nc < 0:
                        continue
                    try:
                        seen = state[nr][nc]
                    except IndexError:
                        break
                    if seen == '.':
                        continue
                    elif seen == '#':
                        occupied += 1
                    break
            if occupied >= tolerance and seat == '#':
                new_state[r][c] = 'L'
                changed = True
            elif occupied == 0 and seat == 'L':
                new_state[r][c] = '#'
                changed = True

    return new_state, changed


def part1(state):
    changed = True
    while changed:
        state, changed = evolve(state)
    return sum(sum(c == '#' for c in r) for r in state)


def part2(state):
    changed = True
    maxdist = max(len(state), len(state[0]))
    while changed:
        state, changed = evolve(state, maxdist=maxdist, tolerance=5)
    return sum(sum(c == '#' for c in r) for r in state)


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
