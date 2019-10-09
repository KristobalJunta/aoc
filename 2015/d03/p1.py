#!/usr/bin/env python3
import sys
from collections import defaultdict
import operator


visited = defaultdict(int)

movement_map = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
}

coords = (0, 0)
visited[coords] += 1

for line in sys.stdin:
    line = line.strip()

    for char in line:
        coords = tuple(map(sum, zip(coords, movement_map[char])))
        visited[coords] += 1

print(len(list(visited.keys())))
