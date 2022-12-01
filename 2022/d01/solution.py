import fileinput


def get_input():
    return [s.strip() for s in fileinput.input()]


def get_elves(data):
    elves = []
    cur_elf = 0

    for line in data:
        if line:
            val = int(line)
            cur_elf += val
        else:
            elves.append(cur_elf)
            cur_elf = 0

    if cur_elf:
        elves.append(cur_elf)

    return elves


def part1(data):
    elves = get_elves(data)
    return max(elves)


def part2(data):
    elves = get_elves(data)
    top_elves = list(sorted(elves, reverse=True))
    return sum(top_elves[:3])


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
