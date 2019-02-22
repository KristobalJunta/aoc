#!/usr/bin/python3

import sys


def cmp(a, b, op):
    if op == '>':
        return a > b
    elif op == '<':
        return a < b
    elif op == '>=':
        return a >= b
    elif op == '<=':
        return a <= b
    elif op == '!=':
        return a != b
    elif op == '==':
        return a == b


with open('input') as f:
    regs = dict()
    tm = -sys.maxsize - 1

    for l in f.readlines():
        reg, op, val, _, ifreg, ifop, ifval = l.strip().split()
        val = int(val)
        ifval = int(ifval)

        if ifreg not in regs:
            regs[ifreg] = 0
        if reg not in regs:
            regs[reg] = 0

        if cmp(regs[ifreg], ifval, ifop):
            if op == 'inc':
                regs[reg] += val
            else:
                regs[reg] -= val

        tm = max(tm, max(regs.values()))

    print(tm)
