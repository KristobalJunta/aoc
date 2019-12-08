import sys


def is_valid(val: int):
    val = list(map(int, str(val)))
    adjacent_counts = []
    adjacent_count = 0

    for a, b in zip(val[:-1], val[1:]):
        if a > b:
            return False
        elif a == b:
            adjacent_count += 1
        else:
            adjacent_counts.append(adjacent_count)
            adjacent_count = 0

    adjacent_counts.append(adjacent_count)
    adjacent_counts = list(map(lambda x: x + 1, adjacent_counts))
    return 2 in adjacent_counts


# Tests
# print(is_valid(112233))
# print(is_valid(123444))
# print(is_valid(111122))

low, high = list(map(int, sys.stdin.readline().strip().split('-')))
res = sum([is_valid(num) for num in range(low, high + 1)])
print(res)
