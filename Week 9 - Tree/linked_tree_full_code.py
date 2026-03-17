class LinkedTree:
    class Node:
        __slots__ = '_element', '_parent', '_children'
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

    def __init__(self):
        self._root = None
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p):
        node = self._validate(p)
        return len(node._children)

    def children(self, p):
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    def __len__(self):
        return self._size

    def add_child(self, p, e):
        parent_node = self._validate(p) if p else None
        new_node = self.Node(e, parent_node)
        if parent_node:
            parent_node._children.append(new_node)
        else:
            self._root = new_node
        self._size += 1
        return self._make_position(new_node)

    def remove(self, p):
        node = self._validate(p)
        if node is self._root:
            self._root = None
            self._size = 0
            return node._element
        parent = node._parent
        if parent:
            parent._children.remove(node)

        def _remove_subtree(n):
            for child in list(n._children):
                _remove_subtree(child)
            self._size -= 1

        _remove_subtree(node)
        node._parent = node
        return node._element

    def find_element(self, element):
        def _find_recursive(node):
            if node._element == element:
                return self._make_position(node)
            for child in node._children:
                result = _find_recursive(child)
                if result:
                    return result
            return None
        return _find_recursive(self._root) if self._root else None


# ============================================================
# Demo
# ============================================================
t = LinkedTree()

root_pos  = t.add_child(None, 'A')
b_pos     = t.add_child(root_pos, 'B')
c_pos     = t.add_child(root_pos, 'C')
d_pos     = t.add_child(root_pos, 'D')
e_pos     = t.add_child(b_pos, 'E')
f_pos     = t.add_child(b_pos, 'F')
g_pos     = t.add_child(c_pos, 'G')
h_pos     = t.add_child(d_pos, 'H')

print("=== Tree Info ===")
print(f"Size            : {len(t)}")
print(f"Root            : {t.root().element()}")
print(f"Children of A   : {[p.element() for p in t.children(t.root())]}")
print(f"Children of B   : {[p.element() for p in t.children(b_pos)]}")
print(f"num_children(D) : {t.num_children(d_pos)}")
print(f"Parent of E     : {t.parent(e_pos).element()}")

print("\n=== find_element ===")
found = t.find_element('G')
print(f"find 'G' : {found.element() if found else 'Not found'}")
found = t.find_element('Z')
print(f"find 'Z' : {found.element() if found else 'Not found'}")

print("\n=== remove 'B' (and subtree E, F) ===")
removed = t.remove(b_pos)
print(f"Removed         : {removed}")
print(f"Size after      : {len(t)}")
print(f"Children of A   : {[p.element() for p in t.children(t.root())]}")