import sys
from intprog import intprog

code = list(map(int, sys.stdin.readline().strip().split(',')))
print(intprog(code[:], 12, 2))
