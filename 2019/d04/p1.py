import sys


def is_valid(val: int):
    val = list(map(int, str(val)))
    has_same = False

    for a, b in zip(val[:-1], val[1:]):
        if a > b:
            return False
        elif a == b:
            has_same = True

    return has_same


# Tests
# print(is_valid(111123))  # True
# print(is_valid(135679))  # False
# print(is_valid(111111))  # True
# print(is_valid(223450))  # False
# print(is_valid(123789))  # False

low, high = list(map(int, sys.stdin.readline().strip().split('-')))
res = sum([is_valid(num) for num in range(low, high + 1)])
print(res)
