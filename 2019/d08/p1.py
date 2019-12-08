import operator
import sys
from collections import Counter


def make_chunks(val, chunk_size):
    return [val[i : i + chunk_size] for i in range(0, len(val), chunk_size)]


def count_zeros(val):
    cnt = Counter(val)
    return cnt['0']


image = sys.stdin.readline().strip()
im_size = (25, 6)
layers = make_chunks(image, operator.mul(*im_size))
min_layer = min(layers, key=count_zeros)
cnt = Counter(min_layer)
print(cnt['1'] * cnt['2'])
