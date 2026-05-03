# Lab 4: Compare BFT and DFT

from coding.lab.LabQ1 import G1, G2, G3
from coding.lab.LabQ2 import breadth_first_traversal
from coding.lab.LabQ3 import depth_first_traversal

graphs = {'G1': G1, 'G2': G2, 'G3': G3}
start_vertices = ['A', 'B', 'C', 'D', 'E']

print("=" * 50)
print("LAB 4: BFT vs DFT Comparison")
print("=" * 50)
for gname, g in graphs.items():
    for sv in start_vertices:
        if sv in g:
            bft = breadth_first_traversal(g, sv)
            dft = depth_first_traversal(g, sv)
            print(f"{gname} | start={sv}")
            print(f"  BFT → {bft}")
            print(f"  DFT → {dft}")