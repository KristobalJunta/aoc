input = open('input.txt')
freq = 0

for line in input.readlines():
    val = int(line)
    freq += val

print(freq)
