with open('input.txt') as infile:
    freq = 0

    for line in infile.readlines():
        val = int(line)
        freq += val

    print(freq)
