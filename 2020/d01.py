import itertools
import fileinput


def get_input():
    data = [l for l in fileinput.input()]
    data = [int(l) for l in data]
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
