import fileinput

PREAMBLE_SIZE = 25


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    data = [int(s) for s in data]
    return data


def binsum(arr, x):
    arr = sorted(el for el in arr)
    arrlen = len(arr)
    l, r = 0, arrlen - 1
    while l < r:
        s = arr[l] + arr[r]
        if s < x:
            l += 1
        elif s > x:
            r -= 1
        else:
            return True
    return False


def part1(data):
    preamble = data[:PREAMBLE_SIZE]
    for x in data[PREAMBLE_SIZE:]:
        if not binsum(preamble, x):
            return x
        preamble = preamble[1:] + [x]


def part2(data):
    invalid = part1(data)
    prefsum = [data[0]]
    for i, d in enumerate(data[1:], start=1):
        prefsum.append(d + prefsum[i-1])
    for i, x in enumerate(prefsum):
        for j, y in enumerate(reversed(prefsum[:i])):
            if x - y == invalid:
                j = i - j
                ans = sorted(data[j:i + 1])
                return ans[0] + ans[-1]


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
