#!/usr/bin/python3

import re


def garb(s):
    s = re.sub('!.', '', s)
    gs = re.findall('<.*?>', s)
    return sum([len(g) - 2 for g in gs])


with open('input') as f:
    for l in f.readlines():
        l = l.strip()
        print(garb(l), l)
