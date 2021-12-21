import fileinput


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    return data


# 20, 30
# -10, -5


def part1(data):
    y = int(data[0].split('=')[-1].split('..')[0])
    y0 = abs(y) - 1
    max_y = (y0 ** 2 + y0) // 2
    return max_y


def part2(data):
    pass


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
