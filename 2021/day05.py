import fileinput
from collections import defaultdict, namedtuple
from pprint import pprint


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    return data


Point = namedtuple("Point", "x y")


def parse_data(data):
    lines = []
    for s in data:
        a, b = s.split(' -> ')

        a = Point(*list(map(int, a.split(','))))
        b = Point(*list(map(int, b.split(','))))

        lines.append((a, b))

    return lines


def group_lines(lines):
    vert = []
    hor = []
    diag = []

    for a, b in lines:
        if a.x == b.x:
            if a.y > b.y:
                vert.append((b, a))
            else:
                vert.append((a, b))
        elif a.y == b.y:
            if a.x > b.x:
                hor.append((b, a))
            else:
                if (a, b) not in vert:
                    hor.append((a, b))
        else:
            if a.x > b.x:
                diag.append((b, a))
            else:
                diag.append((a, b))

    return vert, hor, diag


def part1(data):
    lines = parse_data(data)
    vert, hor, _ = group_lines(lines)

    points = defaultdict(int)

    for a, b in hor:
        for x in range(a.x, b.x + 1):
            points[(x, a.y)] += 1

    for a, b in vert:
        for y in range(a.y, b.y + 1):
            points[(a.x, y)] += 1

    return sum(1 for x in points.values() if x > 1)


def part2(data):
    lines = parse_data(data)
    vert, hor, diag = group_lines(lines)

    points = defaultdict(int)

    for a, b in hor:
        for x in range(a.x, b.x + 1):
            points[(x, a.y)] += 1

    for a, b in vert:
        for y in range(a.y, b.y + 1):
            points[(a.x, y)] += 1

    for a, b in diag:
        for d in range(b.x - a.x + 1):
            if a.y < b.y:
                p = (a.x + d, a.y + d)
            else:
                p = (a.x + d, a.y - d)

            points[p] += 1

    # for k, v in points.items():
    #     s = '*' if v > 1 else ''
    #     print(k, v, s)

    return sum(1 for x in points.values() if x > 1)


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
