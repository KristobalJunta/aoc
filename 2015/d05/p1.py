#!/usr/bin/env python3
import sys
from collections import Counter
from string import ascii_lowercase

vowels = "aeiou"
lines = list(filter(bool, [line.strip() for line in sys.stdin]))
doubles = [a + b for a, b in zip(ascii_lowercase, ascii_lowercase)]
nice_strings = 0

for line in lines:
    letter_counts = Counter(line)
    has_vowels = sum([letter_counts[v] for v in vowels]) >= 3
    has_double = any([d in line for d in doubles])
    has_bad_strings = any([s in line for s in ["ab", "cd", "pq", "xy"]])

    is_nice = has_vowels and has_double and not has_bad_strings
    if is_nice:
        nice_strings += 1

print(nice_strings)
