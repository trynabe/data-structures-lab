class GeneralTree:

    # Create Node
    class _Node:
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

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        return p._node

    # __init__ — สร้าง tree เปล่า โดยกำหนด _root = None และ _size = 0
    def __init__(self):
        self._root = None
        self._size = 0

    # root() — คืนค่า position ของ root node
    def root(self):
        return self._make_position(self._root)

    # parent(p) — รับ position p แล้วคืนค่า position ของ parent ของมัน
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    # num_children(p) — คืนจำนวน children ของ node ที่ตำแหน่ง p
    def num_children(self, p):
        node = self._validate(p)
        return len(node._children)

    # children(p) — วน loop ผ่าน children ทั้งหมดของ node p แล้ว yield ออกมาทีละตัว (เป็น generator)
    def children(self, p):
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    # __len__ — คืนจำนวน node ทั้งหมดใน tree
    def __len__(self):
        return self._size

    def _add_root(self, e):
        self._root = self._Node(e)
        self._size = 1
        return self._make_position(self._root)

    def _add_child(self, p, e):
        node = self._validate(p)
        child = self._Node(e, parent=node)
        node._children.append(child)
        self._size += 1
        return self._make_position(child)


# Tester
tree = GeneralTree()
root = tree._add_root("A")
b = tree._add_child(root, "B")
c = tree._add_child(root, "C")
d = tree._add_child(root, "D")
e = tree._add_child(b, "E")
f = tree._add_child(b, "F")

print(tree.root().element())        # A
print(tree.parent(b).element())     # A
print(tree.num_children(root))      # 3
print(len(tree))                    # 6
for child in tree.children(root):
    print(child.element())          # B C D
