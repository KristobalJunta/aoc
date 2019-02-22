#!/usr/bin/python3

with open('d5.in') as f:
    maze = list(map(lambda x: int(x), f.readlines()))
    i = 0
    n = len(maze)
    k = 0
    while i < n:
        oldi = i
        i = i + maze[i]
        if maze[oldi] > 2:
            maze[oldi] -= 1
        else:
            maze[oldi] += 1
        k += 1

print(k)
