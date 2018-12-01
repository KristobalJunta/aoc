input = open('input.txt')
freqs = set()
freq = 0

freqs.add(0)
lines = input.readlines()

while True:
    for line in lines:
        val = int(line)
        freq += val

        if freq in freqs:
            print(freq)
            exit()

        freqs.add(freq)
