#!/usr/bin/env python3
import math
import sys
from collections import deque


lines = [line.strip() for line in sys.stdin]
masses = deque(map(int, lines))

total_fuel = 0

while masses:
    mass = masses.popleft()
    add_mass = math.floor(mass / 3) - 2
    if add_mass > 0:
        total_fuel += add_mass
        masses.append(add_mass)

print(total_fuel)
