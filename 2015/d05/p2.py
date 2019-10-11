#!/usr/bin/env python3
import sys
from collections import Counter
from string import ascii_lowercase
from itertools import product

lines = list(filter(bool, [line.strip() for line in sys.stdin]))
doubles = [a + b for a, b in zip(ascii_lowercase, ascii_lowercase)]
nice_strings = 0

def has_doubles(line):
    return any([d in line for d in doubles])

for line in lines:
    letter_counts = Counter(line)
    possible_pairs = list(zip(*(iter(line),) * 2)) + list(zip(*(iter(line[1:]),) * 2))
    possible_pairs = [a + b for a, b in possible_pairs]
    has_pairs = any([line.count(p) >= 2 for p in possible_pairs])

    has_same = any([has_doubles(line[::2]), has_doubles(line[1::2])])

    is_nice = has_pairs and has_same
    if is_nice:
        nice_strings += 1

print(nice_strings)
