import fileinput
import operator


def onlydigit(lines):
    return [[c for c in line if c.isdigit()] for line in lines]


def get_input():
    data = [s.removesuffix('\n') for s in fileinput.input()]
    data = list(filter(None, data))
    return data


def part1(data):
    return sum(
        map(
            int,
            (line[0] + line[-1] for line in onlydigit(data))
        )
    )


def part2(data):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers_d = {num: str(idx) for idx, num in enumerate(numbers, 1)}

    lines = []

    for line in data:
        l_nums = list(
            sorted(
                ((num, line.find(num)) for num in numbers if num in line),
                key=operator.itemgetter(1)
            )
        )

        if l_nums:
            num, _ = l_nums[0]
            line: str = line.replace(num, "{}{}".format(numbers_d[num], num), 1)

            r_nums = list(
                sorted(
                    ((num, line.rfind(num)) for num in numbers if num in line),
                    key=operator.itemgetter(1),
                    reverse=True
                )
            )

            num, idx = r_nums[0]
            line = line[:idx] + numbers_d[num] + line[idx:]

        lines.append(line)

    return part1(lines)


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
