import operator


def manh(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


with open('input.txt') as infile:
    points = [tuple(map(int, line.split(','))) for line in infile.readlines()]

thresh = 10000

max_x = max(points, key=operator.itemgetter(0))[0]
max_y = max(points, key=operator.itemgetter(1))[1]

field = [[0] * (max_y+1) for _ in range(max_x+1)]

for x in range(max_x+1):
    for y in range(max_y+1):
        field[x][y] = sum([manh((x, y), point) for point in points])

print(sum([len(list(filter(lambda el: el < thresh, row))) for row in field]))
