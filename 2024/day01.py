import fileinput
import collections


def get_input():
    return list(
        map(
            lambda s: tuple(map(int, str.split(s))),
            filter(None, (s.removesuffix("\n") for s in fileinput.input())),
        )
    )


def part1(arr1, arr2):
    return sum(map(lambda x: abs(x[0] - x[1]), zip(sorted(arr1), sorted(arr2))))


def part2(arr1, arr2):
    count = collections.Counter(arr2)
    return sum(x * count[x] for x in arr1)


if __name__ == "__main__":
    indata = get_input()

    arr1 = []
    arr2 = []

    for a, b in indata:
        arr1.append(a)
        arr2.append(b)

    print(part1(arr1, arr2))
    print(part2(arr1, arr2))
