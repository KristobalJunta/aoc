#!/usr/bin/env python3
import math
import sys


lines = [line.strip() for line in sys.stdin]
masses = list(map(int, lines))

total_fuel = sum([math.floor(mass / 3) - 2 for mass in masses])
print(total_fuel)
