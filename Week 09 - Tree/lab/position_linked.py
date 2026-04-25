class Tree:
    class Position:
        """Abstract base class for position."""
        def element(self):
            raise NotImplementedError
        def __eq__(self, other):
            raise NotImplementedError


class LinkedTree(Tree):

    class _Node:
        # Structure node in memory
        def __init__(self, element, parent=None):
            self._element = element
            self._parent  = parent
            self._children = []

    class Position(Tree.Position):
        """Wrapper for a node's position."""

        def __init__(self, container, node):
            self._container = container  # ต้นไม้ที่ node นี้อยู่
            self._node      = node       # node จริงๆ (ซ่อนไว้)

        def element(self):
            return self._node._element   # ดึงค่าผ่าน wrapper

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    # ── Helper Make Position ──────────────────────
    def _make_position(self, node):
        return self.Position(self, node) if node else None

    def __init__(self):
        root_node  = self._Node("A")
        left_node  = self._Node("B", root_node)
        right_node = self._Node("C", root_node)
        root_node._children = [left_node, right_node]
        self._root = root_node

    def root(self):
        return self._make_position(self._root)

    def children(self, p):
        return [self._make_position(c) for c in p._node._children]

    def parent(self, p):
        return self._make_position(p._node._parent)


# Output
tree = LinkedTree()

root = tree.root()
kids = tree.children(root)
left, right = kids[0], kids[1]

print(root.element())          # → A
print(left.element())           # → B
print(right.element())          # → C

parent_of_left = tree.parent(left)
print(parent_of_left.element()) # → A

print(left == right)            # → False
print(root == parent_of_left)   # → True