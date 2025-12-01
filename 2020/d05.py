import fileinput
from typing import List


def get_input():
    data = [l.strip() for l in fileinput.input()]
    data = list(filter(bool, data))
    return data


def binsearch(s, l, r):
    m = (r + l) // 2
    for c in s:
        if c in 'FL':
            r = m
        if c in 'RB':
            l = m + 1
        m = (r + l) // 2
    return m


def get_id(brdpass):
    row, seat = brdpass[:7], brdpass[7:]
    row = binsearch(row, 0, 127)
    seat = binsearch(seat, 0, 7)
    return row * 8 + seat


def part1(data: List[str]):
    return max(get_id(brdpass) for brdpass in data)


def part2(data):
    seats = sorted(get_id(brdpass) for brdpass in data)
    for idx, seat in enumerate(seats):
        if seat - idx != seats[0]:
            return seat - 1

if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print(part2(indata))
