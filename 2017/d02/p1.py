#!/usr/bin/python3

with open('d2.in') as f:
    chksum = 0
    for line in f:
        arr = list(map(lambda x: int(x), line.strip().split()))
        chksum = chksum + (max(arr) - min(arr))

print(chksum)

