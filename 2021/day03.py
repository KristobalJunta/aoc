import fileinput


def get_input():
    data = [s.strip() for s in fileinput.input()]
    data = list(filter(bool, data))
    return data


def part1(nums):
    nbits = len(nums[0])
    nnums = len(nums)

    gamma = [
        '1' if sum(
            n[bitpos] == '1' for n in nums
        ) > nnums / 2 else '0'
        for bitpos in range(nbits)
    ]
    epsilon = [
        '1' if x == '0' else '0' for x in gamma
    ]

    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)

    print(gamma, epsilon)
    return gamma * epsilon


def part2(nums):
    nbits = len(nums[0])
    oxy = [*nums]
    co2 = [*nums]

    for bitpos in range(nbits):
        valcount = sum(n[bitpos] == '1' for n in oxy)
        if valcount >= len(oxy) / 2:
            val = '1'
        else:
            val = '0'

        oxy = [x for x in oxy if x[bitpos] == val]

        if len(oxy) == 1:
            break

    for bitpos in range(nbits):
        valcount = sum(n[bitpos] == '0' for n in co2)
        if valcount <= len(co2) / 2:
            val = '0'
        else:
            val = '1'

        co2 = [x for x in co2 if x[bitpos] == val]

        if len(co2) == 1:
            break

    oxy = int(oxy.pop(), 2)
    co2 = int(co2.pop(), 2)

    print(oxy, co2)

    return oxy * co2


if __name__ == '__main__':
    indata = get_input()
    print(part1(indata))
    print("*****************")
    print(part2(indata))
