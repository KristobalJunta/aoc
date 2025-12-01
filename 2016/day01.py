import math


def get_input():
    with open('test.txt') as f:
        data = f.read()

    data = data.strip().split(',')
    data = [s.strip() for s in data]
    return data


def vec_add(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return [x1 + x2, y1 + y2]


def manh_dist(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return abs(x1 - x2) +abs(y1 - y2)


def part1(data):
    cur_pos = [0, 0]
    cur_face = 0
    dirs = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]

    for item in data:
        d, step = item[0], int(item[1:])
        if d == 'L':
            cur_face = (cur_face - 1) % 4
        else:
            cur_face = (cur_face + 1) % 4

        idx = (cur_face + 1) % 2
        new_vec = dirs[cur_face]
        new_vec[idx] = new_vec[idx] * step
        cur_pos = vec_add(cur_pos, new_vec)

    print(cur_pos)
    print(manh_dist([0, 0], cur_pos))


data = get_input()
part1(data)
