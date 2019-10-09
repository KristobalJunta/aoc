#!/usr/bin/env python3
import sys

def rotate(l, n):
    return l[-n:] + l[:-n]

total_ribbon = 0
lines = [line.strip() for line in sys.stdin]
lines = list(filter(bool, lines))
for line in lines:
    dims = list(map(int, line.split("x")))
    min_perimeter = min([a+b for ])

print(total_area)
