import fileinput
from typing import List
import string


def get_input():
    data = [l.strip() for l in fileinput.input()]
    return data


def part1(data: List[str]):
    res = 0
    answers = set()
    for line in data:
        if not line:
            res += len(answers)
            answers = set()
        else:
            answers |= set(line)
    res += len(answers)
    return res


def part2(data):
    res = 0
    answers = set(string.ascii_lowercase)
    for line in data:
        if not line:
            res += len(answers)
            answers = set(string.ascii_lowercase)
        else:
            answers &= set(line)
    res += len(answers)
    return res


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
