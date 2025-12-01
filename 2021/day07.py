import fileinput
import math
import functools


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(map(int, data.pop(0).split(',')))
    return data


@functools.lru_cache
def prog_sum(n, a1, an):
    return int(n * (a1 + an) / 2)


def fuel_cost(origin, dest):
    return abs(dest - origin)


def fuel_cost2(origin, dest):
    n = abs(dest - origin)
    return prog_sum(n, 1, n)


def find_best(data, cost_func):
    fuel = math.inf
    bestpos = -1

    # goal is to minimize fuel value which is function from position
    # brute force solution for finding best postition doesn't seem optimal

    for pos in range(data[0], data[-1] + 1):
        curval = sum(cost_func(x, pos) for x in data)

        if curval < fuel:
            bestpos = pos
            fuel = curval

    return fuel, bestpos


if __name__ == '__main__':
    data = sorted(get_input())
    print(find_best(data, fuel_cost))
    print(find_best(data, fuel_cost2))
