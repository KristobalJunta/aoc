# O(log n) solution:
# https://www.reddit.com/r/adventofcode/comments/a2damm/2018_day2_part_2_a_linear_time_solution/eaxco3u/

from collections import Counter

with open('input.txt') as infile:
    ids = infile.readlines()
    twos = 0
    threes = 0
    for item in ids:
        counts = dict(Counter(item))
        two, three = 0, 0

        for count in counts.values():
            if count == 2:
                two = 1
            if count == 3:
                three = 1

        twos += two
        threes += three

    checksum = twos * threes
    print(checksum)
