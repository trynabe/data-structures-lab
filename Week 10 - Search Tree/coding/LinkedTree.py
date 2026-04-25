from collections import deque # ใช้สำหรับ Breadth-First Traversal
from LinkedBinaryTree import LinkedTree, Position

# ==========================================
# ส่วนที่ 1: โครงสร้างต้นไม้แบบ Binary Tree พื้นฐาน
# ==========================================
class LinkedBinaryTree(LinkedTree):
    """คลาสพื้นฐานสำหรับต้นไม้ที่มีลูกได้ไม่เกิน 2 ตัว (ซ้าย-ขวา)"""
    
    def add_left(self, p, e):
        """เพิ่มข้อมูล e ไปเป็นลูกฝั่งซ้ายของตำแหน่ง p"""
        node = self._validate(p) # ตรวจสอบว่าตำแหน่ง p มีอยู่จริง
        if len(node._children) > 0: # ถ้ามีลูกฝั่งซ้ายอยู่แล้วให้แจ้งเตือน Error
            raise ValueError("Left child already exists!")
        return self.add_child(p, e)

    def add_right(self, p, e):
        """เพิ่มข้อมูล e ไปเป็นลูกฝั่งขวาของตำแหน่ง p"""
        node = self._validate(p)
        if len(node._children) > 1: # ถ้ามีลูกฝั่งขวาอยู่แล้วให้แจ้งเตือน Error
            raise ValueError("Right child already exists!")
        return self.add_child(p, e)

    def left(self, p):
        """ดึงตำแหน่งของลูกฝั่งซ้ายออกมา"""
        node = self._validate(p)
        return next(iter(self.children(p)), None)

    def right(self, p):
        """ดึงตำแหน่งของลูกฝั่งขวาออกมา"""
        node = self._validate(p)
        children = list(self.children(p))
        return children[1] if len(children) > 1 else None

    # --- โค้ดสำหรับการท่องไปในต้นไม้ (Tree Traversals) ---
    def preorder_traversal(self, p):
        """การท่องแบบ Preorder: ราก → ซ้าย → ขวา"""
        if p:
            print(p.element(), end=' -> ')
            self.preorder_traversal(self.left(p))
            self.preorder_traversal(self.right(p))

    def breadth_first_traversal(self):
        """การท่องแบบ Breadth-First: กวาดดูทีละชั้น (Level-order)"""
        if self.is_empty():
            return
        queue = deque([self.root()]) # ใช้คิว (Queue) เข้ามาช่วย
        while queue:
            p = queue.popleft()
            print(p.element(), end=' -> ')
            for child in self.children(p):
                queue.append(child)


# ==========================================
# ส่วนที่ 2: โครงสร้าง Binary Search Tree (BST)
# ==========================================
class BinarySearchTree(LinkedBinaryTree):
    """คลาส Binary Search Tree ที่สืบทอดมาจาก LinkedBinaryTree อีกที"""

    def insert(self, p, e):
        """ฟังก์ชันสำหรับ 'เพิ่ม' ข้อมูลเข้าไปในต้นไม้ โดยต้องรักษากฎของ BST (ซ้ายน้อยกว่า ขวามากกว่า)"""
        if p is None:
            return self.add_child(None, e) # ถ้าต้นไม้ยังว่าง ให้ใส่เป็นราก (Root)
        
        node = self._validate(p)
        if e < node._element: # ถ้าค่าที่เข้ามา น้อยกว่า ค่าในโหนดปัจจุบัน ให้ไปทาง 'ซ้าย'
            if not self.left(p):
                return self.add_left(p, e) # ถ้าซ้ายว่าง ใส่ได้เลย
            else:
                return self.insert(self.left(p), e) # ถ้าไม่ว่าง ให้เรียกตัวเองวนซ้ำเพื่อลงไปลึกขึ้น
        else: # ถ้าค่าที่เข้ามา มากกว่า ค่าในโหนดปัจจุบัน ให้ไปทาง 'ขวา'
            if not self.right(p):
                return self.add_right(p, e) # ถ้าขวาว่าง ใส่ได้เลย
            else:
                return self.insert(self.right(p), e) # ถ้าไม่ว่าง เรียกตัวเองวนซ้ำลงไปฝั่งขวา

    def search(self, p, e):
        """ฟังก์ชันสำหรับ 'ค้นหา' ข้อมูล"""
        if p is None:
            return None # ค้นหาจนสุดทางแล้วไม่เจอ (Element not found)
        
        node = self._validate(p)
        if e == node._element:
            return p # เจอแล้ว! ส่งคืนตำแหน่งนั้น
        elif e < node._element:
            return self.search(self.left(p), e) # ถ้าน้อยกว่า ค้นหาต่อทางฝั่งซ้าย
        else:
            return self.search(self.right(p), e) # ถ้ามากกว่า ค้นหาต่อทางฝั่งขวา

    def _find_min(self, p):
        """หาค่าที่น้อยที่สุดในฝั่งขวา (ใช้ช่วยตอนลบโหนด)"""
        current = p
        while self.left(current): # วิ่งไปทางซ้ายเรื่อยๆ จนสุดทาง
            current = self.left(current)
        return current

    def delete(self, p):
        """ฟังก์ชันสำหรับ 'ลบ' ข้อมูลออกจากต้นไม้"""
        node = self._validate(p)

        # กรณีที่ 1: เป็น Leaf Node (ไม่มีลูกเลย) - ลบทิ้งได้เลย
        if len(node._children) == 0:
            parent = node._parent
            if parent:
                parent._children.remove(node)
            else:
                self._root = None # กรณีตัวที่ลบคือ Root Node
            self._size -= 1
            return node._element

        # กรณีที่ 2: มีลูกแค่ 1 ตัว - เอาลูกขึ้นมาแทนที่ตัวเอง
        elif len(node._children) == 1:
            child = node._children[0]
            parent = node._parent
            if parent:
                index = parent._children.index(node)
                parent._children[index] = child # เอาลูกเสียบแทน
                child._parent = parent
            else:
                self._root = child
                child._parent = None
            self._size -= 1
            return node._element

        # กรณีที่ 3: มีลูก 2 ตัว - ต้องหาตัวแทน (Inorder Successor) มาสวมรอย
        else:
            successor = self._find_min(self.right(p)) # หาตัวน้อยสุดฝั่งขวา
            node._element = successor._element # ก๊อปปี้ค่ามาทับโหนดที่จะลบ
            return self.delete(successor) # ลบตัวแทนทิ้งซะ

    def inorder_traversal(self, p):
        """การท่องแบบ Inorder สำหรับ BST (ซ้าย → ราก → ขวา) ผลลัพธ์จะได้ข้อมูลเรียงจากน้อยไปมาก!"""
        if p:
            self.inorder_traversal(self.left(p))
            print(p.element(), end=' <- ')
            self.inorder_traversal(self.right(p))