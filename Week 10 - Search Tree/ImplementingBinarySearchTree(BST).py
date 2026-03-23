# ── BinarySearchTree (Page 44) ────────────────────────────

class Node:
    def __init__(self, element, parent=None):
        self._element  = element
        self._parent   = parent
        self._children = []

class Position:
    def __init__(self, container, node):
        self._container = container
        self._node      = node

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

    def root(self):     return self._make_position(self._root)
    def is_empty(self): return self._size == 0

    def children(self, p):
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    def add_child(self, p, e):
        if p is None:
            self._root = Node(e)
            self._size += 1
            return self._make_position(self._root)
        node  = self._validate(p)
        child = Node(e, node)
        node._children.append(child)
        self._size += 1
        return self._make_position(child)


class LinkedBinaryTree(LinkedTree):

    def add_left(self, p, e):
        node = self._validate(p)
        if len(node._children) > 0:
            raise ValueError("Left child already exists!")
        return self.add_child(p, e)

    def add_right(self, p, e):
        node = self._validate(p)
        if len(node._children) > 1:
            raise ValueError("Right child already exists!")
        return self.add_child(p, e)

    def left(self, p):
        self._validate(p)
        return next(iter(self.children(p)), None)

    def right(self, p):
        self._validate(p)
        children = list(self.children(p))
        return children[1] if len(children) > 1 else None

    def _find_min(self, p):
        current = p
        while self.left(current):
            current = self.left(current)
        return current

    def delete(self, p):
        node = self._validate(p)
        # Case 1: Node is a leaf (no children)
        if len(node._children) == 0:
            parent = node._parent
            if parent: parent._children.remove(node)
            else:      self._root = None
            self._size -= 1
            return node._element
        # Case 2: Node has one child
        elif len(node._children) == 1:
            child  = node._children[0]
            parent = node._parent
            if parent:
                index = parent._children.index(node)
                parent._children[index] = child
                child._parent = parent
            else:
                self._root    = child
                child._parent = None
            self._size -= 1
            return node._element
        # Case 3: Node has two children
        else:
            successor     = self._find_min(self.right(p))
            node._element = successor.element()
            return self.delete(successor)


# ── BinarySearchTree (Page 44) ────────────────────────────

class BinarySearchTree(LinkedBinaryTree):
    """Binary Search Tree (BST) extending LinkedBinaryTree."""

    def insert(self, p, e):
        """Insert an element into the BST while maintaining BST order."""
        if p is None:
            return self.add_child(None, e)   # Empty tree -> insert as root

        node = self._validate(p)
        if e < node._element:                # Less than -> go left
            if not self.left(p):
                return self.add_left(p, e)   # Empty slot -> insert here
            else:
                return self.insert(self.left(p), e)   # Recurse left
        else:                                # Greater than -> go right
            if not self.right(p):
                return self.add_right(p, e)
            else:
                return self.insert(self.right(p), e)

    def search(self, p, e):
        """Search for an element in the BST and return its Position."""
        if p is None:
            return None                      # Not found

        node = self._validate(p)
        if e == node._element:
            return p                         # Found it!
        elif e < node._element:
            return self.search(self.left(p), e)    # Search left subtree
        else:
            return self.search(self.right(p), e)   # Search right subtree

    def inorder_traversal(self, p):
        """Inorder Traversal: Left → Root → Right (Results in sorted order)"""
        if p:
            self.inorder_traversal(self.left(p))
            print(p.element(), end=' → ')
            self.inorder_traversal(self.right(p))


# ── Test Cases ─────────────────────────────────────────────
#
#        50
#       /  \
#     30    70
#    /  \  /  \
#   20  40 60  80

bst  = BinarySearchTree()
root = bst.insert(None, 50)
bst.insert(root, 30)
bst.insert(root, 70)
bst.insert(root, 20)
bst.insert(root, 40)
bst.insert(root, 60)
bst.insert(root, 80)

print("=" * 45)
print("Inserting: 50, 30, 70, 20, 40, 60, 80")
print("=" * 45)

print("\nInorder traversal (Sorted):")
print("  ", end="")
bst.inorder_traversal(bst.root())
print("end")

print("\nSearch Operations:")
for val in [40, 99]:
    result = bst.search(bst.root(), val)
    if result:
        print(f"  search({val}) → Found node: {result.element()}")
    else:
        print(f"  search({val}) → Not found")

print("\nDeleting 30 (Node with 2 children):")
n30 = bst.search(bst.root(), 30)
bst.delete(n30)
print("  Inorder after deletion: ", end="")
bst.inorder_traversal(bst.root())
print("end")

print("\nDeleting 20 (Leaf node):")
n20 = bst.search(bst.root(), 20)
bst.delete(n20)
print("  Inorder after deletion: ", end="")
bst.inorder_traversal(bst.root())
print("end")
print("=" * 45)