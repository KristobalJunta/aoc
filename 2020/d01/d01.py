import itertools


def get_input():
    with open('2020/d01/input.txt') as f:
        data = f.read()
    data = [int(l) for l in data.splitlines()]
    return data

def part1(data):
    for a, b in itertools.product(data, repeat=2):
        if a + b == 2020:
            return a * b

def part2(data):
    for a, b, c in itertools.product(data, repeat=3):
        if sum([a, b, c]) == 2020:
            return a * b * c

if __name__ == '__main__':
    indata = get_input()

    res1 = part1(indata)
    res2 = part2(indata)

    print(res1)
    print(res2)
