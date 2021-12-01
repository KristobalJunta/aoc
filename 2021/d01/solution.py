from functools import reduce
import fileinput


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    data = list(map(int, data))
    return data


def part1(data):
    res = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            res += 1

    return res


def part2(data):
    pref = [data[0]]
    for i in range(1, len(data)):
        pref.append(data[i] + pref[i-1])

    pref = [0] + pref
    sums = []
    for i in range(3, len(pref)):
        sums.append(
            pref[i] - pref[i-3]
        )

    return part1(sums)


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))

