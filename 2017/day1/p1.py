#!/usr/bin/python3

with open('d1p1.in') as f:
    numstr = f.read().strip()
    sum = 0
    for i in range(0, len(numstr)-1):
        if numstr[i] == numstr[i+1]:
            sum += int(numstr[i])
    if numstr[-1] == numstr[0]:
        sum += int(numstr[0])

    print(sum)

