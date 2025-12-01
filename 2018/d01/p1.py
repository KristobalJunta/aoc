# efficient solution:
# https://www.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/eaukxu5/

with open('input.txt') as infile:
    freq = 0

    for line in infile.readlines():
        val = int(line)
        freq += val

    print(freq)
