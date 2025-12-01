import fileinput


def get_input():
    data = [s.removesuffix('\n') for s in fileinput.input()]
    data = list(filter(None, data))
    return data


def part1(data):
    for buffer in data:
        for pos in range(3, len(buffer)):
            marker = buffer[pos - 3 : pos + 1]
            if len(set(marker)) == len(marker):
                print(pos + 1)
                break


def part2(data):
    for buffer in data:
        for pos in range(13, len(buffer)):
            marker = buffer[pos - 13 : pos + 1]
            if len(set(marker)) == len(marker):
                print(pos + 1)
                break


if __name__ == '__main__':
    indata = get_input()
    print("### p1")
    part1(indata)

    print("### p2")
    part2(indata)
