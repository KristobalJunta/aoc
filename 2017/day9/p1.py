#!/usr/bin/python3

import re


def clean(s):
    s = re.sub('!.', '', s)
    s = re.sub('<.*?>', '', s)
    s = re.sub('(?<!}),', '', s)
    return s


def score(s):
    k = 0
    res = 0
    for c in s:
        if c == '{':
            k += 1
        if c == '}':
            res += k
            k -= 1

    return res


with open('input') as f:
    for l in f.readlines():
        l = clean(l.strip())
        print(score(l), l)
