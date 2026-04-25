# Node = โหนดจริงในต้นไม้ เก็บข้อมูล + parent + children
class Node:
    def __init__(self, element, parent=None):
        self._element  = element      # ค่าที่เก็บใน node
        self._parent   = parent       # pointer ไปหา parent
        self._children = []           # list เก็บลูก (ใช้แทน left/right)

# Position = ตัว wrapper ครอบ Node เพื่อป้องกัน user เข้าถึง node ตรง ๆ
class Position:
    def __init__(self, container, node):
        self._container = container   # อ้างถึง tree ที่มันอยู่
        self._node      = node        # node จริง

    def element(self):
        return self._node._element    # คืนค่าข้อมูลใน node

    def __eq__(self, other):
        # เช็คว่า Position นี้กับอีกตัวชี้ node เดียวกันไหม
        return type(other) is type(self) and other._node is self._node


# Tree พื้นฐาน (ยังไม่ใช่ BST)
class LinkedTree:
    def __init__(self):
        self._root = None             # root ของ tree
        self._size = 0                # จำนวน node

    def _validate(self, p):
        # ตรวจว่า p เป็น Position ที่ถูกต้อง
        if not isinstance(p, Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        return p._node                # คืน node จริง

    def _make_position(self, node):
        # แปลง node -> Position
        return Position(self, node) if node is not None else None

    def root(self):     
        return self._make_position(self._root)   # คืน root

    def is_empty(self): 
        return self._size == 0                   # เช็ค tree ว่างไหม

    def children(self, p):
        # loop ลูกของ node
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    def add_child(self, p, e):
        # เพิ่มลูก
        if p is None:
            # กรณี tree ว่าง → สร้าง root
            self._root = Node(e)
            self._size += 1
            return self._make_position(self._root)

        node  = self._validate(p)
        child = Node(e, node)        # สร้าง node ใหม่
        node._children.append(child) # เพิ่มเป็นลูก
        self._size += 1
        return self._make_position(child)


# Binary Tree (จำกัดลูก 2 คน)
class LinkedBinaryTree(LinkedTree):

    def add_left(self, p, e):
        node = self._validate(p)
        # ถ้ามีลูกแล้ว = ถือว่า left ถูกใช้
        if len(node._children) > 0:
            raise ValueError("Left child already exists!")
        return self.add_child(p, e)

    def add_right(self, p, e):
        node = self._validate(p)
        # ถ้ามีลูก 2 ตัวแล้ว = right เต็ม
        if len(node._children) > 1:
            raise ValueError("Right child already exists!")
        return self.add_child(p, e)

    def left(self, p):
        self._validate(p)
        # คืนลูกตัวแรก = left
        return next(iter(self.children(p)), None)

    def right(self, p):
        self._validate(p)
        children = list(self.children(p))
        # ลูกตัวที่สอง = right
        return children[1] if len(children) > 1 else None

    def _find_min(self, p):
        # หา node ที่น้อยสุด (ไปซ้ายสุด)
        current = p
        while self.left(current):
            current = self.left(current)
        return current

    def delete(self, p):
        node = self._validate(p)

        # Case 1: ไม่มีลูก (leaf)
        if len(node._children) == 0:
            parent = node._parent
            if parent:
                parent._children.remove(node)  # ลบออกจาก parent
            else:
                self._root = None             # ถ้าเป็น root
            self._size -= 1
            return node._element

        # Case 2: มีลูก 1 ตัว
        elif len(node._children) == 1:
            child  = node._children[0]
            parent = node._parent

            if parent:
                index = parent._children.index(node)
                parent._children[index] = child   # เอาลูกขึ้นแทน
                child._parent = parent
            else:
                self._root    = child            # ถ้าเป็น root
                child._parent = None

            self._size -= 1
            return node._element

        # Case 3: มีลูก 2 ตัว
        else:
            # หา inorder successor (ค่าที่น้อยสุดฝั่งขวา)
            successor     = self._find_min(self.right(p))
            node._element = successor.element()   # เอาค่ามาแทน
            return self.delete(successor)         # ลบ successor แทน


# BST = Binary Search Tree (เรียงซ้าย < root < ขวา)
class BinarySearchTree(LinkedBinaryTree):

    def insert(self, p, e):
        if p is None:
            return self.add_child(None, e)  # tree ว่าง

        node = self._validate(p)

        if e < node._element:
            # ไปซ้าย
            if not self.left(p):
                return self.add_left(p, e)
            else:
                return self.insert(self.left(p), e)
        else:
            # ไปขวา
            if not self.right(p):
                return self.add_right(p, e)
            else:
                return self.insert(self.right(p), e)

    def search(self, p, e):
        if p is None:
            return None  # ไม่เจอ

        node = self._validate(p)

        if e == node._element:
            return p
        elif e < node._element:
            return self.search(self.left(p), e)
        else:
            return self.search(self.right(p), e)

    def inorder_traversal(self, p):
        # ซ้าย → root → ขวา (จะได้ sorted)
        if p:
            self.inorder_traversal(self.left(p))
            print(p.element(), end=' → ')
            self.inorder_traversal(self.right(p))


# ===== TEST =====
bst  = BinarySearchTree()

# สร้าง root
root = bst.insert(None, 50)

# insert ค่าอื่น ๆ
bst.insert(root, 30)
bst.insert(root, 70)
bst.insert(root, 20)
bst.insert(root, 40)
bst.insert(root, 60)
bst.insert(root, 80)

# แสดง inorder (เรียงแล้ว)
bst.inorder_traversal(bst.root())

# search
bst.search(bst.root(), 40)

# delete node ที่มี 2 ลูก
n30 = bst.search(bst.root(), 30)
bst.delete(n30)

# delete leaf
n20 = bst.search(bst.root(), 20)
bst.delete(n20)