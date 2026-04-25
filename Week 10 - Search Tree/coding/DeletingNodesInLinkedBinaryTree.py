# Deleting Nodes in LinkedBinaryTree
# คืออะไร: โปรแกรมสำหรับลบโหนดออกจาก Binary Tree แบบ Linked List
# ทำอะไร:  ลบโหนดในทั้ง 3 กรณี:
#          - Case 1: Leaf Node (ไม่มีลูก)
#          - Case 2: มีลูกแค่ 1 ตัว
#          - Case 3: มีลูก 2 ตัว (ใช้ Inorder Successor)
# ตัวอย่างต้นไม้:
#          50
#         /  \
#       30    70
#      /  \  /  \
#     20  40 60  80

class Node:
    """
    โหนด (Node) - หน่วยพื้นฐานที่เก็บข้อมูล
    - _element: ข้อมูลที่เก็บในโหนด
    - _parent: อ้างอิงไปยังโหนดแม่ (parent node)
    - _children: รายการลูกโหนด (child nodes)
    """
    def __init__(self, element, parent=None):
        self._element  = element
        self._parent   = parent
        self._children = []

class Position:
    """
    ตำแหน่ง (Position) - ตัวแทนของโหนดในต้นไม้
    ใช้สำหรับ:
    - ซ่อนรายละเอียด Node ภายใน
    - ให้ผู้ใช้ระบุตำแหน่งในต้นไม้ได้อย่างปลอดภัย
    - ป้องกันการเข้าถึงโหนดโดยตรง
    """
    def __init__(self, container, node):
        self._container = container
        self._node      = node

    def element(self):
        """ดึงข้อมูลออกจากโหนด"""
        return self._node._element

    def __eq__(self, other):
        """เปรียบเทียบว่า 2 Position เดียวกันหรือไม่"""
        return type(other) is type(self) and other._node is self._node

class LinkedTree:
    """
    ต้นไม้ทั่วไปแบบ Linked List (General Tree)
    - สามารถมีลูกได้กี่ตัวก็ได้ (unlimited children)
    - ใช้ Node และ Position ในการจัดการ
    """
    def __init__(self):
        self._root = None
        self._size = 0

    def _validate(self, p):
        """ตรวจสอบว่า Position ถูกต้องหรือไม่"""
        if not isinstance(p, Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        return p._node

    def _make_position(self, node):
        """สร้าง Position จาก Node"""
        return Position(self, node) if node is not None else None

    def root(self):    
        """ส่งคืน Position ของราก (root)"""
        return self._make_position(self._root)
    
    def is_empty(self): 
        """ตรวจสอบว่าต้นไม้ว่างหรือไม่"""
        return self._size == 0

    def children(self, p):
        """ส่งคืนรายการลูกของ Position p"""
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    def add_child(self, p, e):
        """
        เพิ่มลูกใหม่
        - ถ้า p is None: สร้าง root
        - ถ้า p is not None: เพิ่มเป็นลูกของ p
        """
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
    """
    ต้นไม้ไบนารี่แบบ Linked List (Binary Tree)
    - สืบทอดจาก LinkedTree
    - ลูกได้แค่ 2 ตัว: left (ซ้าย) และ right (ขวา)
    - มีฟังก์ชัน delete สำหรับลบโหนดได้แบบมี 3 กรณี
    """

    def add_left(self, p, e):
        """เพิ่มลูกฝั่งซ้าย (ถ้ายังไม่มี)"""
        node = self._validate(p)
        if len(node._children) > 0:
            raise ValueError("Left child already exists!")
        return self.add_child(p, e)

    def add_right(self, p, e):
        """เพิ่มลูกฝั่งขวา (ถ้ายังไม่มี)"""
        node = self._validate(p)
        if len(node._children) > 1:
            raise ValueError("Right child already exists!")
        return self.add_child(p, e)

    def left(self, p):
        """ดึง Position ของลูกฝั่งซ้าย"""
        self._validate(p)
        return next(iter(self.children(p)), None)

    def right(self, p):
        """ดึง Position ของลูกฝั่งขวา"""
        self._validate(p)
        children = list(self.children(p))
        return children[1] if len(children) > 1 else None

    def inorder(self, p, result=None):
        """
        ท่องต้นไม้แบบ Inorder (ซ้าย → ราก → ขวา)
        - ผลลัพธ์จะได้ลำดับเรียงจากน้อยไปมาก (สำหรับ BST)
        """
        if result is None: result = []
        if p:
            self.inorder(self.left(p), result)
            result.append(str(p.element()))
            self.inorder(self.right(p), result)
        return result

    def _find_min(self, p):
        """
        หา Node ที่มีค่าน้อยที่สุด (เดินซ้ายจนสุด)
        ใช้ช่วยในการลบโหนดที่มีลูก 2 ตัว
        (หาตัวแทน = Inorder Successor)
        """
        current = p
        while self.left(current):
            current = self.left(current)
        return current

    def delete(self, p):
        """
        ฟังก์ชันลบโหนด - จัดการ 3 กรณี:
        - Case 1: Leaf Node (ไม่มีลูก) → ลบทิ้งได้เลย
        - Case 2: มีลูกแค่ 1 ตัว → เอาลูกขึ้นมาแทนที่
        - Case 3: มีลูก 2 ตัว → หา Inorder Successor ก๊อปค่ามาแทน ลบตัวแทน
        """
        node = self._validate(p)

        # Case 1: Leaf node (ไม่มีลูก)
        if len(node._children) == 0:
            parent = node._parent
            if parent:
                parent._children.remove(node)
            else:
                # ถ้าเป็น root ก็ให้ต้นไม้เป็นว่าง
                self._root = None
            self._size -= 1
            return node._element

        # Case 2: มีลูกแค่ 1 ตัว
        elif len(node._children) == 1:
            child  = node._children[0]
            parent = node._parent
            if parent:
                # เสียบลูกเข้าแทนโหนดที่ลบ
                index = parent._children.index(node)
                parent._children[index] = child
                child._parent = parent
            else:
                # ถ้าเป็น root ให้ลูกขึ้นมาเป็น root
                self._root    = child
                child._parent = None
            self._size -= 1
            return node._element

        # Case 3: มีลูก 2 ตัว
        else:
            # หา Inorder Successor (ค่าน้อยสุดในฝั่งขวา)
            successor     = self._find_min(self.right(p))
            # ก๊อปค่ามาทับโหนดที่ต้องการลบ
            node._element = successor.element()
            # ลบตัวแทน (successor มักจะเป็น Case 1 หรือ 2)
            return self.delete(successor)


# ส่วนที่ 3: สร้างต้นไม้และทดสอบ

def build():
    """
    สร้างต้นไม้ตัวอย่าง:
           50
          /  \
        30    70
       /  \  /  \
      20  40 60  80
    """
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
    """แสดงเนื้อหาของต้นไม้ (Inorder traversal)"""
    print(f"  {label}: {' → '.join(bt.inorder(bt.root()))}")


# การทดสอบ: Case 1 - ลบ Leaf Node
print("Case 1: ลบ Leaf Node (20)")
bt = build()
show(bt, "ก่อนลบ")
bt.delete(bt.left(bt.left(bt.root())))
show(bt, "หลังลบ")

print()

# การทดสอบ: Case 2 - ลบ Node ที่มีลูก 1 ตัว
print("Case 2: ลบ Node ที่มีลูก 1 ตัว (30)")
bt2  = LinkedBinaryTree()
r    = bt2.add_child(None, 50)
n30b = bt2.add_left(r, 30)
n70b = bt2.add_right(r, 70)
bt2.add_right(n30b, 40)        # 30 มีแค่ลูกขวา
bt2.add_left(n70b, 60)
bt2.add_right(n70b, 80)
show(bt2, "ก่อนลบ")
bt2.delete(n30b)
show(bt2, "หลังลบ")

print()

# การทดสอบ: Case 3 - ลบ Node ที่มีลูก 2 ตัว (Root)
print("Case 3: ลบ Node ที่มีลูก 2 ตัว (50 - Root)")
bt3  = build()
root = bt3.root()
show(bt3, "ก่อนลบ")
bt3.delete(root)
show(bt3, "หลังลบ")