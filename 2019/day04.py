import sys


low, high = list(map(int, sys.stdin.readline().strip().split('-')))

# part 1
def is_valid(val: int):
    val = list(map(int, str(val)))
    has_same = False

    for a, b in zip(val[:-1], val[1:]):
        if a > b:
            return False
        elif a == b:
            has_same = True

    return has_same

## Tests
# print(is_valid(111123))  # True
# print(is_valid(135679))  # False
# print(is_valid(111111))  # True
# print(is_valid(223450))  # False
# print(is_valid(123789))  # False

res = sum([is_valid(num) for num in range(low, high + 1)])
print(res)


# part 2
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


## Tests
# print(is_valid(112233))
# print(is_valid(123444))
# print(is_valid(111122))

res = sum([is_valid(num) for num in range(low, high + 1)])
print(res)
