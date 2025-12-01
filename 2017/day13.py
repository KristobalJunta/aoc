#!/usr/bin/python3

with open('input') as f:
    lrs = list()
    for l in f.readlines():
        lrs.append(l)

    lrs = list(map(lambda s: list(map(lambda x: int(x), s.split(': '))), [s for s in lrs]))

    svrs = 0
    for lr in lrs:
        d, r = lr

    print(svrs)
