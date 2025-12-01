import fileinput
from math import floor
from collections import defaultdict, Counter


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = [int(x) for x in data[0].split(',')]
    return data


def spawn(d, s):
    """Count how many offspring will be spawned in `d` days by fish with counter `s`"""
    return floor((d + 6 - s) / 7)


def model_lanternfish(data, d):
    """Play game of life for fish"""
    res = len(data)

    # d - number of days
    # s - initial counter value
    # n - number of fish with same counter value
    fish = [(d, s, n) for s, n in Counter(data).items()]
    born = defaultdict(int)

    def spawn2(dx, s, n):
        """
        Count how many offspring will be spawned in `dx` days
        by `n` fishes with internal counter of `s`
        """
        num_children = spawn(dx, s)
        fish_ttl = []

        for k in range(num_children):
            birthday = (s + 1) + 7 * k
            ttl = dx - (8 + birthday)

            if ttl > 0:
                fish_ttl.append(ttl)

        for ttl, nx in Counter(fish_ttl).items():
            born[ttl] += n * nx

        return num_children * n

    # calculate offspring for initial fishes
    res = sum(spawn2(di, s, n) for di, s, n in fish)

    # calculate all next genreations
    # this works efficiently because each TTL value is processed only once
    # processed in descending order, each TTL will only produce values less than itself
    # (TTL is number of days fish will be active before d-day)
    while born:
        ttl, num_fish = sorted(born.items(), key=lambda x: x[0], reverse=True).pop(0)
        res += spawn2(ttl, 0, num_fish)
        del born[ttl]

    return res


if __name__ == '__main__':
    data = get_input()

    for d in (18, 80, 256):
        output = model_lanternfish(data, d)
        print(f"After {d:>3} day(s): {output}")
