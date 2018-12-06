import operator
from collections import defaultdict, Counter


def manh(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


with open('input.txt') as infile:
    points = [tuple(map(lambda s: int(s.strip()), line.split(','))) for line in infile.readlines()]

max_x = max(points, key=operator.itemgetter(0))[0]
max_y = max(points, key=operator.itemgetter(1))[1]
min_x = min(points, key=operator.itemgetter(0))[0]
min_y = min(points, key=operator.itemgetter(1))[1]

field = [[-1] * (max_y+1) for _ in range(max_x+1)]

for x in range(max_x+1):
    for y in range(max_y+1):
        dist = defaultdict(lambda: [])
        for idx, point in enumerate(points):
            d = manh((x, y), point)
            dist[d].append(idx)

        min_dist, pts = min(dist.items(), key=operator.itemgetter(0))
        field[x][y] = pts[0] if len(pts) == 1 else -1

edge_points = set(field[0] + field[-1] + [row[0] for row in field] + [row[-1] for row in field])

result = dict()
for row in field:
    claims = dict(Counter(filter(lambda el: el != -1, row)))
    merge = set([el for el in set(result) | set(claims) if el not in edge_points])
    result = {k: result.get(k, 0) + claims.get(k, 0) for k in merge}

print('\n'.join([','.join(map(lambda cell: str(cell).rjust(2), row)) for row in field]))  # print field
print(max(Counter(result).items(), key=operator.itemgetter(1)))
