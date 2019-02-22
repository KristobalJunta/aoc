#!/usr/bin/python3

import re


with open('d7.in') as f:
    roots = set()
    childs = set()

    for l in f:
        l = re.split("\s\(\d+\)\s", l)
        l[1] = l[1].strip().strip('-> ').split(', ')
        roots.add(l[0])

        for v in l[1]:
            childs.add(v)

print(list(set.difference(roots, childs))[0])

