#!/usr/bin/env python3
import sys
import operator
from functools import reduce

def rotate(l, n):
    return l[-n:] + l[:-n]

total_area = 0
lines = [line.strip() for line in sys.stdin]
lines = list(filter(bool, lines))

print("part 1")

for line in lines:
    dims = list(map(int, line.split("x")))
    area = sum(2*a*b for a, b in zip(dims, rotate(dims, 1)))
    slack = min([a*b for a, b in zip(dims, rotate(dims, 1))])
    total_area += area + slack

print(total_area)

print("part 2")

total_ribbon = 0

for line in lines:
    dims = list(map(int, line.split("x")))
    min_perimeter = min([2 * (a + b) for a, b in zip(dims, rotate(dims, 1))])
    volume = reduce(operator.mul, dims, 1)
    total_ribbon += min_perimeter + volume

print(total_ribbon)
