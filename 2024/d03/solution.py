import fileinput
import re
import operator


def get_input():
    return list(filter(None, (s.removesuffix('\n') for s in fileinput.input())))


mul_re = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
do_re = re.compile(r"do\(\)")
dont_re = re.compile(r"don't\(\)")


def part1(data):
    res = 0

    for line in data:
        patterns = re.findall(mul_re, line)
        res += sum(int(x) * int(y) for x, y in patterns)

    return res


def part2(data):
    res = 0

    for line in data:
        do_pos = [m.start() for m in re.finditer(do_re, line)]
        dont_pos = [m.start() for m in re.finditer(dont_re, line)]

        # At the beginning of the program, mul instructions are enabled
        do_pos.insert(0, 0)
        dont_pos.append(len(line))

        dont_do = dict()

        for dp in do_pos:
            for dnp in dont_pos:
                if dnp > dp:
                    if dnp not in dont_do:
                        dont_do[dnp] = dp
                    break

        do_dont = {v:k for k, v in dont_do.items()}

        print(line)

        do_str = list(" " * (len(line) + 1))
        for x in do_pos:
            do_str[x] = "*"
        for x in dont_pos:
            do_str[x] = "x"
        print(''.join(do_str))

        print("do", do_pos)
        print("dont", dont_pos)
        from pprint import pprint
        pprint(do_dont)

        print()

        res += sum(
            operator.mul(*map(int, mul.groups()))
            for mul in re.finditer(mul_re, line)
            if any(start < mul.start() < end for start, end in do_dont.items())
        )

    return res


if __name__ == "__main__":
    indata = get_input()

    print(part1(indata))
    print(part2(indata))
