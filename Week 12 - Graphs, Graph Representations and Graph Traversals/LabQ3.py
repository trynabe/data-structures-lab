# Lab 3: Depth-First Traversal

from LabQ1 import G1, G2, G3

def depth_first_traversal(graph, start):
    visited = []
    stack = [start]
    seen = set()

    while stack:
        vertex = stack.pop()
        if vertex not in seen:
            seen.add(vertex)
            visited.append(vertex)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in seen:
                    stack.append(neighbor)
    return visited


graphs = {'G1': G1, 'G2': G2, 'G3': G3}
start_vertices = ['A', 'B', 'C', 'D', 'E']

print("=" * 50)
print("LAB 3: Depth-First Traversal")
print("=" * 50)
for gname, g in graphs.items():
    for sv in start_vertices:
        if sv in g:
            result = depth_first_traversal(g, sv)
            print(f"{gname} | start={sv} → {result}")