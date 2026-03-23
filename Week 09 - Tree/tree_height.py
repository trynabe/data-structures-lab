class Node: 
    def __init__(self, element, parent=None):
        self.element = element
        self.parent = parent
        self.children = []

class SimpleTree:
    def __init__(self, root_node):
        self.root = root_node

    def is_leaf(self, p):
        return len(p.children) == 0
    
    def children(self, p):
        return p.children
    
    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
        
root = Node("Electronics R'Us")
rd = Node("R&D", parent=root)
sales = Node("Sales", parent=root)
purchasing = Node("Purchasing", parent=root)
mfg = Node("Manufacturing", parent=root)

root.children = [rd, sales, purchasing, mfg]

intl = Node("Internation", parent=sales)
sales.children = [Node("Domestic", parent=sales), intl]

overseas = Node("Overseas", parent=intl)
intl.children = [Node("Canada", parent=intl), Node("S. America", parent=intl), overseas]

africa = Node("Africa", parent=overseas)
overseas.children = [africa, Node("Europe", parent=overseas), Node("Asia", parent=overseas), Node("Austalia", parent=overseas)]

my_tree = SimpleTree(root)

print(f"Height of Root: {my_tree._height2(root)}")
print(f"Height of Overseas: {my_tree._height2(overseas)}")
print(f"Height of Africa: {my_tree._height2(africa)}")