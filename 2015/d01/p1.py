#!/usr/bin/env python3
import sys

data = sys.stdin.read().replace("\n", "").strip()
floor_diffs = [1 if c == '(' else -1 for c in data]
print(sum(floor_diffs))
