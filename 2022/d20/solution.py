import fileinput
from copy import copy


def get_input():
    data = [s.removesuffix('\n') for s in fileinput.input()]
    data = list(filter(None, data))
    data = [int(x) for x in data]
    return data


def part1(data):
    res = copy(data)

    def mix(seq, pos):
        return seq

    for idx in range(len(res)):
        res = mix(res, idx)



def part2(data):
    pass


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
