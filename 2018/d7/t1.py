import operator
import re


with open('input.txt') as infile:
    lines = infile.readlines()

vertices = dict()
edges = []

for line in lines:
    v_from, v_to = re.search('^Step (\w).*before step (\w)', line).groups()
    edges.append((v_from, v_to))
    vertices[v_from] = vertices.get(v_from, 0)
    vertices[v_to] = vertices.get(v_to, 0) + 1

print(len(edges))

ans = []

while len(edges):
    next_vertex = sorted(filter(lambda v: v[1] == 0, vertices.items()), key=operator.itemgetter(0))
    next_vertex = next_vertex[0][0]
    ans.append(next_vertex)
    vertices[next_vertex] -= 1
    for v_from, v_to in list(filter(lambda e: e[0] == next_vertex, edges)):
        vertices[v_to] -= 1
        edges.remove((v_from, v_to))

ans += sorted([key for key, val in vertices.items() if val == 0])
print(''.join(ans))
