class Node: 
    def __init__(self, element, parent=None):
        self.element = element
        self.parent = parent
        self.children = []

class SimpleTree:
    def __init__(self, root_node):
        self.root = root_node

    def is_root(self, p):
        return p == self.root
    
    def parent(self, p):
        return p.parent
    
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
electronics = Node("Electornics R'Us")
sales = Node("Sales", parent=electronics)
international = Node("International", parent=sales)
overseas = Node("Overseas", parent=international)

tree = SimpleTree(electronics)

print(f"Depth of Electronics: {tree.depth(electronics)}")
print(f"Depth of International: {tree.depth(international)}")
print(f"Depth of Overseas: {tree.depth(overseas)}")