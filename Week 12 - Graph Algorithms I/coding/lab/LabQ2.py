# Lab 2: Breadth-First Traversal

from collections import deque
from coding.lab.LabQ1 import G1, G2, G3

def breadth_first_traversal(graph, start):
    visited = []
    queue = deque([start])
    seen = {start}

    while queue:
        vertex = queue.popleft()
        visited.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return visited


graphs = {'G1': G1, 'G2': G2, 'G3': G3}
start_vertices = ['A', 'B', 'C', 'D', 'E']

print("=" * 50)
print("LAB 2: Breadth-First Traversal")
print("=" * 50)
for gname, g in graphs.items():
    for sv in start_vertices:
        if sv in g:
            result = breadth_first_traversal(g, sv)
            print(f"{gname} | start={sv} → {result}")