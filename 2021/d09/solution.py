import fileinput
from collections import deque


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    data = [[int(x) for x in row] for row in data]
    return data


def valid_coord(x, y, w, h):
    return 0 <= x <= w - 1 and 0 <= y <= h - 1


steps = ((1, 0), (0, 1), (-1, 0), (0, -1))


def part1(data):
    w, h = len(data), len(data[0])
    res = 0

    lowpoints = []

    for i in range(w):
        for j in range(h):
            el = data[i][j]
            isrisk = True

            for dx, dy in steps:
                x = i + dx
                y = j + dy

                if valid_coord(x, y, w, h):
                    isrisk = isrisk and el < data[x][y]

            if isrisk:
                lowpoints.append((i, j))
                res += 1 + el

    return lowpoints, res


def basin_size(data, start):
    w, h = len(data), len(data[0])
    visited = set()
    q = deque([start])

    res = 0

    while q:
        i, j = q.popleft()
        el = data[i][j]

        print(i, j, el, visited)

        visited.add((i, j))

        if el == 9:
            continue

        res += 1

        for dx, dy in steps:
            point = (i + dx, j + dy)

            if valid_coord(*point, w, h) and point not in visited:
                q.append(point)

    return res

def part2(data, lowpoints):
    basins = []

    for point in lowpoints:
        print("start basin at", point)
        basins.append(basin_size(data, point))

        # break

    return basins
    return sorted(basins, reverse=True)[:3]


if __name__ == "__main__":
    data = get_input()
    lowpoints, res1 = part1(data)
    print(res1)

    res2 = part2(data, lowpoints)
    print(res2)
