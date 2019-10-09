#!/usr/bin/env python3
import sys
from itertools import accumulate

data = sys.stdin.read().replace("\n", "").strip()
floor_diffs = [1 if c == '(' else -1 for c in data]
ans = list(accumulate(floor_diffs)).index(-1) + 1
print(ans)
