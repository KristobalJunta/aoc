import fileinput


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    data = [int(s.split().pop()) for s in data]
    return data


def part1(data):
    p1, p2 = data


def part2(data):
    pass


if __name__ == "__main__":
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
