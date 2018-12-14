import operator
import re


class Worker:
    finish = 0
    task = ''

    def __repr__(self):
        return str([self.task, self.finish])


a = ord('A') - 1
num_workers = 2
workers = []
duration = 0

for _ in range(num_workers):
    workers.append(Worker())

with open('input.txt') as infile:
    lines = infile.readlines()

vertices = dict()
edges = []

for line in lines:
    v_from, v_to = re.search('^Step (\w).*before step (\w)', line).groups()
    edges.append((v_from, v_to))
    vertices[v_from] = vertices.get(v_from, 0)
    vertices[v_to] = vertices.get(v_to, 0) + 1

ans = []
t = 0

while len(edges):
    print(t)

    ready = sorted(filter(lambda v: v[1] == 0, vertices.items()), key=operator.itemgetter(0))
    print(ready)

    for next_vertex, _ in ready:
        idx, w = min(enumerate(workers), key=lambda el: el[1].finish)
        if w.finish <= t:
            workers[idx].task = next_vertex
            workers[idx].finish += ord(next_vertex) - a + duration

            ans.append(next_vertex)
            vertices[next_vertex] -= 1

    print(workers)
    t = min(filter(lambda w: w.finish > 0, workers), key=lambda w: w.finish).finish

    for v_from, v_to in list(filter(lambda e: e[0] == next_vertex, edges)):
        vertices[v_to] -= 1
        edges.remove((v_from, v_to))

vs = sorted([key for key, val in vertices.items() if val == 0])
for v in vs:
    pass

print(''.join(ans))
