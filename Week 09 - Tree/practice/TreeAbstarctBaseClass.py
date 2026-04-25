class Tree:

    class Position:

        def element(self):
            raise NotImplementedError('must be implemented by subclass')
    
    # Returns root position.
    def root(self):
        raise NotImplementedError('must be implemented by subclass')
    
    # Returns parent of p.
    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    # Number of children of p.
    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    # Iterates over children.
    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    # Returns total elements in tree.
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
    
    # Checks if p is root.
    def is_root(self, p):
        return self.root() == p
    
    # Checks if p is a leaf.
    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    # Checks if tree is empty.
    def is_empty(self):
        return len(self == 0)
    
class SimpleTree(Tree):
    def __init__(self, data):
        self._data = data
        self._children = []
        self._parent = None

    def element(self):
        return self._data
    
    def root(self):
        return self
    
    def num_children(self, p):
        return len(p._children)
    
    def children(self, p):
        return iter(p._children)
    
    def __len__(self):
        return 1 + sum(len(c) for c in self._children)

    def add_child(self, child):
        child._parent = self
        self._children.append(child)

if __name__ == "__main__":
    # 1. Create Tree
    ceo = SimpleTree("CEO")
    manager = SimpleTree("Manager")
    intern = SimpleTree("Intern")

    # 2. Build Structure
    ceo.add_child(manager)
    manager.add_child(intern)

    # 3. Output Result
    print("--- Tree Analysis Results ---")
    print(f"Root Element: {ceo.element()}")
    print(f"Is CEO the root? : {ceo.is_root(ceo)}")
    print(f"Is Manager a leaf? : {ceo.is_leaf(manager)}")
    print(f"Is Intern a leaf? : {ceo.is_leaf(intern)}")
    print(f"Total nodes in tree: {len(ceo)}")