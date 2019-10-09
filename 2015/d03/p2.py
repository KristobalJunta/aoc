#!/usr/bin/env python3
import sys
from collections import defaultdict
import operator


visited = defaultdict(int)
moves = ["santa", "robosanta"]

movement_map = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
}

coords = {
    "santa": (0, 0),
    "robosanta": (0, 0),
}

move = moves[0]
visited[coords[move]] += 1

lines = [line.strip() for line in sys.stdin]
idx = 0
for line in lines:
    for char in line:
        move = moves[idx % 2]
        coords[move] = tuple(map(sum, zip(coords[move], movement_map[char])))
        visited[coords[move]] += 1
        idx += 1

print(len(list(visited.keys())))
