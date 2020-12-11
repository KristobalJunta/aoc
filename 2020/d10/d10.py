import fileinput


def get_input():
    data = [l.strip() for l in fileinput.input()]
    data = list(filter(bool, data))
    return data


def preprocess(data):
    jolts = sorted(int(v) for v in data)
    jolts = [0, *jolts, jolts[-1] + 3]
    return jolts


def part1(data):
    diffs = []
    jolts = preprocess(data)
    for i, x in enumerate(jolts):
        for y in jolts[i+1:]:
            d = y - x
            assert d < 4
            diffs.append(d)
            break
    a, b = diffs.count(1), diffs.count(3)
    return a * b


def part2(data):
    jolts = preprocess(data)
    combos = [0] * len(jolts)
    combos[0] = combos[1] = 1
    for i in range(2, len(jolts)):
        x = jolts[i]
        for j in range(i-1, -1, -1):
            y = jolts[j]
            if x - y > 3:
                break
            combos[i] += combos[j]
    return combos[-1]


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
