import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point<{self.x},{self.y}>"


class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Segment<{self.start}; {self.end}>"

    def __len__(self):
        return distance(self.start, self.end)


class Intersection:
    def __init__(self, point, steps=0):
        self.point = point
        self.steps = steps


def distance(a: Point, b: Point):
    """Find Manhattan distance between two points"""
    return abs(a.x - b.x) + abs(a.y - b.y)


def build_segments(wire):
    wire_segments = []
    point = Point(0, 0)
    new_point = point

    for item in wire:
        direction = item[0]
        dist = int(item[1:])
        if direction == "U":
            new_point = point + Point(0, dist)
        if direction == "D":
            new_point = point + Point(0, -dist)
        if direction == "L":
            new_point = point + Point(-dist, 0)
        if direction == "R":
            new_point = point + Point(dist, 0)

        wire_segments.append(Segment(point, new_point))
        point = new_point

    return wire_segments


def vertical(s: Segment):
    """Return True if segment is vertical, False if horizontal-"""
    return s.start.x == s.end.x


def intersect(a: Segment, b: Segment):
    """Find point of intersection between horizontal and vertical segments"""
    if vertical(a) and not vertical(b):
        return intersect(b, a)

    x_intersect = b.start.x in range(*sorted([a.start.x, a.end.x]))
    y_intersect = a.start.y in range(*sorted([b.start.y, b.end.y]))

    if x_intersect and y_intersect:
        return Point(b.start.x, a.start.y)

    return None


wires = [line.strip().split(',') for line in sys.stdin.readlines()]
segments = [build_segments(wire) for wire in wires]

intersections = []
for i, a in enumerate(segments[0]):
    for j, b in enumerate(segments[1]):
        p = intersect(a, b)
        if p is not None:
            steps_a = sum(len(s) for s in segments[0][:i] + [Segment(a.start, p)])
            steps_b = sum(len(s) for s in segments[1][:j] + [Segment(b.start, p)])
            steps = steps_a + steps_b
            intersections.append(Intersection(p, steps))

answer = min(
    distance(Point(0, 0), intersection.point)
    for intersection in intersections
)

print("part 1")
print(answer)

answer = min(intersection.steps for intersection in intersections)

print("part 2")
print(answer)
