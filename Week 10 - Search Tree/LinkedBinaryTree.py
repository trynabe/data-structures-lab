class Node:
    def __init__(self, element, parent=None):
        self._element = element
        self._parent = parent
        self._children = []

class Position:
    def __init__(self, container, node):
        self._container = container
        self._node = node

    def element(self):
        return self._node._element

    def __eq__(self, other):
        return type(other) is type(self) and other._node is self._node

class LinkedTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        return p._node

    def _make_position(self, node):
        return Position(self, node) if node is not None else None

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def children(self, p):
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    def add_child(self, p, e):
        if p is None:
            self._root = Node(e)
            self._size += 1
            return self._make_position(self._root)
        node = self._validate(p)
        child = Node(e, node)
        node._children.append(child)
        self._size += 1
        return self._make_position(child)

    def is_empty(self):
        return self._size == 0

class LinkedBinaryTree(LinkedTree):
    """Binary tree implementation extending LinkedTree."""

    def add_left(self, p, e):
        """Add a left child to Position p; raise error if left child exists."""
        node = self._validate(p)
        if len(node._children) > 0:
            raise ValueError("Left child already exists!")
        return self.add_child(p, e)

    def add_right(self, p, e):
        """Add a right child to Position p; raise error if right child exists."""
        node = self._validate(p)
        if len(node._children) > 1:
            raise ValueError("Right child already exists!")
        return self.add_child(p, e)

    def left(self, p):
        """Return Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return next(iter(self.children(p)), None)

    def right(self, p):
        """Return Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        children = list(self.children(p))
        return children[1] if len(children) > 1 else None

bt = LinkedBinaryTree()
root = bt.add_child(None, "A")

b = bt.add_left(root, "B")
c = bt.add_right(root, "C")
d = bt.add_left(b, "D")
e = bt.add_right(b, "E")
f = bt.add_right(c, "F")

print("=== tree structure ===")
print(f"Root:         {root.element()}")
print(f"left(root):   {bt.left(root).element()}")
print(f"right(root):  {bt.right(root).element()}")
print(f"left(B):      {bt.left(b).element()}")
print(f"right(B):     {bt.right(b).element()}")
lc = bt.left(c)
rc = bt.right(c)
print(f"left(C):      {lc.element() if lc else None}")
print(f"right(C):     {rc.element() if rc else None}")
