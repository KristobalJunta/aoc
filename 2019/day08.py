import operator
import sys
from collections import Counter


def make_chunks(val, chunk_size):
    return [val[i : i + chunk_size] for i in range(0, len(val), chunk_size)]


def count_zeros(val):
    cnt = Counter(val)
    return cnt["0"]


image = sys.stdin.readline().strip()
im_size = (25, 6)
layers = make_chunks(image, operator.mul(*im_size))


# part 1
min_layer = min(layers, key=count_zeros)
cnt = Counter(min_layer)
print(cnt["1"] * cnt["2"])


# part 2
result = []

for i in range(operator.mul(*im_size)):
    pix_vals = [layer[i] for layer in layers]
    pix_vals = list(filter(lambda v: v != "2", pix_vals))

    if pix_vals:
        final_val = pix_vals[0]
    else:
        final_val = "2"

    result.append(final_val)

result = "".join(result)
print(result)
result = result.replace("0", " ")
result_chunks = make_chunks(result, im_size[0])
print()
print("\n".join(result_chunks))
