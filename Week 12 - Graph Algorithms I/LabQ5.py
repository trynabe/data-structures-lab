from LabQ1 import G1, G2, G3

def transform_to_matrix(graph):
    nodes = sorted(list(graph.keys()))
    matrix = []
    
    for i in nodes:
        row = []
        for j in nodes:
            if j in graph[i]:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
        
    return nodes, matrix

def print_matrix(nodes, matrix):
    print("".join(nodes))
    for i in range(len(nodes)):
        row_str = "".join(str(val) for val in matrix[i])
        print(f"{nodes[i]}{row_str}")

graph_bonus = dict()
graph_bonus['A'] = ['B', 'C']
graph_bonus['B'] = ['A', 'C', 'D', 'E']
graph_bonus['C'] = ['A', 'B', 'D']
graph_bonus['D'] = ['B', 'C', 'D', 'E']
graph_bonus['E'] = ['B', 'D']

print("=" * 50)
print("LAB 5: Transform Adjacency List to Adjacency Matrix")
print("=" * 50)

print("Example Graph from Slide:")
nodes_b, matrix_b = transform_to_matrix(graph_bonus)
print_matrix(nodes_b, matrix_b)
print("-" * 20)

print("G1 Matrix:")
nodes_1, matrix_1 = transform_to_matrix(G1)
print_matrix(nodes_1, matrix_1)