#!/usr/bin/python3

def findnum(arr):
    for i in arr: 
        for j in arr:
            if i == j:
                pass
            elif max(i,j) % min(i,j) == 0:
                return max(i,j) // min(i,j)

with open('d2.in') as f:
    chksum = 0
    for line in f:
        arr = list(map(lambda x: int(x), line.strip().split()))
        chksum += findnum(arr)

print(chksum)

