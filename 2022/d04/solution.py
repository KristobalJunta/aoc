import fileinput


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    new_data = []

    for line in data:
        elf1, elf2 = line.split(',')

        a, b = [int(e) for e in elf1.split('-')]
        x, y = [int(e) for e in elf2.split('-')]

        new_data.append((a,b,x,y))

    return new_data


def part1(data):
    count = 0

    for a,b,x,y in data:
        if (a >= x and b <= y) or (x >= a and y <= b):
            count += 1

    return count


def part2(data):
    count = 0

    for a,b,x,y in data:
        if (
            (x <= a <= y) or
            (x <= b <= y) or
            (a <= x <= b) or
            (a <= y <= b)
        ):
            count += 1

    return count


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
