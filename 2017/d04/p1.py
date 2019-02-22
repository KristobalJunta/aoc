#!/usr/bin/python3

with open('d4.in') as f:
    cn = 0
    for l in f:
        w = l.strip().split()
        if len(w) == len(set(w)):
            cn += 1

print(cn)

