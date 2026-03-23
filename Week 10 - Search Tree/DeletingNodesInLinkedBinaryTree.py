# ── Deleting Nodes in LinkedBinaryTree ───────────────────
#
#           50
#          /  \
#        30    70
#       /  \  /  \
#      20  40 60  80

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

    def root(self):    return self._make_position(self._root)
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

    def inorder(self, p, result=None):
        if result is None: result = []
        if p:
            self.inorder(self.left(p), result)
            result.append(str(p.element()))
            self.inorder(self.right(p), result)
        return result

    # ── search inorder successor (pages 31) ───────────────────

    def _find_min(self, p):
        """หา node ที่เล็กที่สุดใน subtree (เดินซ้ายจนสุด)"""
        current = p
        while self.left(current):
            current = self.left(current)
        return current

    # ── delete all 3 case (pages 28-30) ──────────────────

    def delete(self, p):
        node = self._validate(p)

        # Case 1: Leaf node (not has child)
        if len(node._children) == 0:
            parent = node._parent
            if parent:
                parent._children.remove(node)
            else:
                self._root = None
            self._size -= 1
            return node._element

        # Case 2: has 1 child
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

        # Case 3: have 2 child → use inorder successor
        else:
            successor     = self._find_min(self.right(p))
            node._element = successor.element()
            return self.delete(successor)


# ── create tree and test ───────────────────────────────────

def build():
    bt   = LinkedBinaryTree()
    root = bt.add_child(None, 50)
    n30  = bt.add_left(root, 30)
    n70  = bt.add_right(root, 70)
    bt.add_left(n30, 20)
    bt.add_right(n30, 40)
    bt.add_left(n70, 60)
    bt.add_right(n70, 80)
    return bt

def show(bt, label):
    print(f"  {label}: {' → '.join(bt.inorder(bt.root()))}")


# Case 1: del leaf (20)
print("Case 1: del Leaf node (20)")
bt = build()
show(bt, "before to del")
bt.delete(bt.left(bt.left(bt.root())))
show(bt, "after to del")

print()

# Case 2: del node 1 child (30 with only a right foot 40)
print("Case 2: del node 1 child (30)")
bt2  = LinkedBinaryTree()
r    = bt2.add_child(None, 50)
n30b = bt2.add_left(r, 30)
n70b = bt2.add_right(r, 70)
bt2.add_right(n30b, 40)
bt2.add_left(n70b, 60)
bt2.add_right(n70b, 80)
show(bt2, "before to del")
bt2.delete(n30b)
show(bt2, "after to del")

print()

# Case 3: del node 2 child (root 50)
print("Case 3: del node 2 child (50)")
bt3  = build()
root = bt3.root()
show(bt3, "before to del")
bt3.delete(root)
show(bt3, "after to del")