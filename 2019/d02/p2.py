import itertools
import sys
from intprog import intprog


code = list(map(int, sys.stdin.readline().strip().split(',')))

for noun, verb in itertools.product(range(0, 100), repeat=2):
    result = intprog(code[:], noun, verb)
    if result == 19690720:
        print(noun * 100 + verb)
