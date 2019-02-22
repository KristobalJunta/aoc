#!/usr/bin/python3

f = open('d1p1.in')
numstr = f.read().strip()
# numstr = input()
sum = 0
l = len(numstr)
step = l // 2

for i in range(0, len(numstr)):
    if i + step > l - 1:
        ind = step - l + i
    else:
        ind = i + step

    if numstr[i] == numstr[ind]:
        sum += int(numstr[i])

print(sum)

