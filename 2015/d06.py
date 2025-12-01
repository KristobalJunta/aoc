#!/usr/bin/env python3
import sys
from collections import namedtuple


Coords = namedtuple("Coords", "x y")
Rect = namedtuple("Rect", "op lb rt")


def part1(inp):
    lights = [[False] * 1000 for _ in range(1000)]

    def apply_op(op, x, y):
        if op == "toggle":
            lights[x][y] = not lights[x][y]
        if op == "turn off":
            lights[x][y] = False
        if op == "turn on":
            lights[x][y] = True

    for line in inp:
        line = line.replace("through ", "")
        op, lb, rt = line.rsplit(maxsplit=2)
        lb = Coords(*map(int, lb.split(",")))
        rt = Coords(*map(int, rt.split(",")))
        rect = Rect(op, lb, rt)

        for i in range(rect.lb.x, rect.rt.x + 1):
            for j in range(rect.lb.y, rect.rt.y + 1):
                apply_op(rect.op, i, j)

    result = sum([sum(map(int, row)) for row in lights])
    print(result)


def part2(inp):
    lights = [[False] * 1000 for _ in range(1000)]

    def apply_op(op, x, y):
        if op == "toggle":
            lights[x][y] = lights[x][y] + 2
        if op == "turn off":
            lights[x][y] = max(lights[x][y] - 1, 0)
        if op == "turn on":
            lights[x][y] = lights[x][y] + 1

    for line in inp:
        line = line.replace("through ", "")
        op, lb, rt = line.rsplit(maxsplit=2)
        lb = Coords(*map(int, lb.split(",")))
        rt = Coords(*map(int, rt.split(",")))
        rect = Rect(op, lb, rt)

        for i in range(rect.lb.x, rect.rt.x + 1):
            for j in range(rect.lb.y, rect.rt.y + 1):
                apply_op(rect.op, i, j)

    result = sum([sum(row) for row in lights])
    print(result)


if __name__ == "__main__":
    lines = list(filter(bool, [line.strip() for line in sys.stdin]))
    part1(lines)
    print()
    part2(lines)
