# Base class defining Tree properties (Reference: Slide 33)
class Tree:
    class Position:
        """Abstraction representing the location of a single element."""
        def element(self):
            raise NotImplementedError()
        def __eq__(self, other):
            raise NotImplementedError()

    # Abstract methods to be implemented by subclasses [cite: 589]
    def root(self):
        raise NotImplementedError()
    def parent(self, p):
        raise NotImplementedError()
    def num_children(self, p):
        raise NotImplementedError()
    def children(self, p):
        raise NotImplementedError()
    def __len__(self):
        raise NotImplementedError()

    # Concrete methods implemented directly in the base class [cite: 505, 589]
    def is_root(self, p):
        return self.root() == p
    def is_leaf(self, p):
        return self.num_children(p) == 0
    def is_empty(self):
        return len(self) == 0

    # Computing Depth: Number of ancestors excluding p itself [cite: 510, 515]
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    # Computing Height: Recursive O(n) complexity [cite: 542, 568]
    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None: p = self.root()
        return self._height2(p)

# Linked Structure implementation (Reference: Slides 35-39)
class LinkedTree(Tree):
    class _Node:
        """Internal node structure for the linked tree[cite: 611, 625]."""
        __slots__ = '_element', '_parent', '_children'
        def __init__(self, element, parent=None):
            self._element = element
            self._parent = parent
            self._children = []

    class Position(Tree.Position):
        """Wrapper for a node's position to enforce encapsulation[cite: 636, 639]."""
        def __init__(self, container, node):
            self._container = container
            self._node = node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            return isinstance(other, type(self)) and other._node is self._node

    def _validate(self, p):
        """Ensures the Position is valid and belongs to this tree[cite: 642, 644]."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node: # Indicates a deprecated (removed) node
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Creates a Position object for safe navigation[cite: 643]."""
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        """Initialize an empty tree[cite: 680]."""
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size
        
    def root(self):
        return self._make_position(self._root)
        
    def parent(self, p):
        return self._make_position(self._validate(p)._parent)
        
    def num_children(self, p):
        return len(self._validate(p)._children)
        
    def children(self, p):
        """Iterates through child positions[cite: 680]."""
        for child in self._validate(p)._children:
            yield self._make_position(child)

    # Method to add nodes (Input Logic) [cite: 682]
    def add_child(self, p, e):
        """Add a new child with element 'e' to node at position 'p'."""
        parent_node = self._validate(p) if p else None
        new_node = self._Node(e, parent_node)
        if parent_node:
            parent_node._children.append(new_node)
        else:
            if self._root is not None:
                raise ValueError('Root already exists')
            self._root = new_node
        self._size += 1
        return self._make_position(new_node)

    # Search method using Depth-First Search (DFS) [cite: 688, 703]
    def find_element(self, element):
        """Find and return the Position of the node containing 'element'."""
        def _find_recursive(node):
            if node._element == element:
                return self._make_position(node)
            for child in node._children:
                result = _find_recursive(child)
                if result:
                    return result
            return None
        return _find_recursive(self._root) if self._root else None

# --- INPUT AND OUTPUT SECTION ---
if __name__ == "__main__":
    print("--- Creating Corporate Hierarchy (Electronics R'Us) ---")
    lt = LinkedTree()
    
    # Adding Input (Manual Construction) [cite: 301, 727]
    root_pos = lt.add_child(None, "Electronics R'Us") # Level 0
    
    sales = lt.add_child(root_pos, "Sales")           # Level 1
    mfg = lt.add_child(root_pos, "Manufacturing")     # Level 1
    
    lt.add_child(sales, "Domestic")                   # Level 2
    inter = lt.add_child(sales, "International")      # Level 2
    
    lt.add_child(inter, "Canada")                     # Level 3
    overseas = lt.add_child(inter, "Overseas")        # Level 3
    
    lt.add_child(overseas, "Africa")                  # Level 4

    # Displaying Results
    print(f"Total number of nodes: {len(lt)}")
    
    # Testing Depth and Height functions [cite: 514, 543]
    print(f"Depth of Overseas: {lt.depth(overseas)}") # Should be 3 (Root -> Sales -> International -> Overseas)
    print(f"Height of the Tree: {lt.height()}")       # Should be 4 (Path to Africa)

    # Testing Search functionality [cite: 797]
    search_term = "Africa"
    found = lt.find_element(search_term)
    if found:
        print(f"Found '{search_term}'! Location (Depth): {lt.depth(found)}")
    else:
        print(f"'{search_term}' not found")