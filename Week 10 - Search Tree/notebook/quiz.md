# แบบทดสอบเจาะลึก: Search Trees & Code Tracing

## ส่วนที่ 1: คำถาม

### ข้อ 1. พิจารณาโค้ดต่อไปนี้:

```python
bt = LinkedBinaryTree()
root = bt.add_child(None, 'A')
b = bt.add_left(root, 'B')
c = bt.add_right(root, 'C')
d = bt.add_left(b, 'D')

bt.preorder_traversal(root)
```

หากฟังก์ชัน traversal ใช้ `print(..., end=' -> ')` ผลลัพธ์ที่ได้คือข้อใด?
ก) A -> B -> D -> C ->
ข) D -> B -> C -> A ->
ค) D -> B -> A -> C ->
ง) A -> B -> C -> D ->

---

### ข้อ 2.

```python
bt = LinkedBinaryTree()
root = bt.add_child(None, 'A')
b = bt.add_left(root, 'B')
c = bt.add_right(root, 'C')
d = bt.add_left(b, 'D')

bt.inorder_traversal(root)
```

ผลลัพธ์คือข้อใด?
ก) D -> B -> A -> C ->
ข) A -> B -> D -> C ->
ค) B -> D -> C -> A ->
ง) D -> B -> C -> A ->

---

### ข้อ 3.

```python
bt.postorder_traversal(root)
```

ก) A -> B -> C -> D ->
ข) D -> C -> B -> A ->
ค) D -> B -> C -> A ->
ง) B -> D -> A -> C ->

---

### ข้อ 4.

```python
bst = BinarySearchTree()
root = bst.insert(None, 50)
bst.insert(root, 30)
bst.insert(root, 70)
bst.insert(root, 20)

bst.inorder_traversal(root)
```

ก) 50 -> 30 -> 20 -> 70 ->
ข) 20 -> 30 -> 50 -> 70 ->
ค) 20 -> 30 -> 70 -> 50 ->
ง) 70 -> 50 -> 30 -> 20 ->

---

### ข้อ 5.

```python
bst.preorder_traversal(root)
```

ก) 50 -> 30 -> 20 -> 70 ->
ข) 50 -> 70 -> 30 -> 20 ->
ค) 20 -> 30 -> 50 -> 70 ->
ง) 20 -> 70 -> 30 -> 50 ->

---

### ข้อ 6.

```python
bt = LinkedBinaryTree()
root = bt.add_child(None, 'A')
bt.add_left(root, 'B')
bt.add_left(root, 'X')
```

ก) ValueError("Right child already exists!")
ข) ValueError("Left child already exists!")
ค) ไม่มี Error
ง) AttributeError

---

### ข้อ 7.

```python
bst = BinarySearchTree()
root = bst.insert(None, 50)
b = bst.insert(root, 30)
c = bst.insert(root, 70)

bst.delete(c)
bst.inorder_traversal(root)
```

ก) 30 -> 50 -> 70 ->
ข) 50 -> 30 ->
ค) 30 -> 50 ->
ง) Error

---

### ข้อ 8.

```python
bst = BinarySearchTree()
root = bst.insert(None, 50)
b = bst.insert(root, 30)
bst.insert(root, 20)

bst.delete(b)
bst.preorder_traversal(root)
```

ก) 50 -> 20 -> 30 ->
ข) 20 -> 50 ->
ค) 50 -> 20 ->
ง) Error

---

### ข้อ 9.

```python
bst = BinarySearchTree()
root = bst.insert(None, 50)
b = bst.insert(root, 30)
c = bst.insert(root, 70)
bst.insert(root, 60)
bst.insert(root, 80)

bst.delete(c)
bst.preorder_traversal(root)
```

ก) 50 -> 30 -> 60 -> 80 ->
ข) 50 -> 30 -> 80 -> 60 ->
ค) 20 -> 30 -> 50 -> 60 -> 80 ->
ง) 30 -> 50 -> 60 -> 80 ->

---

### ข้อ 10.

```python
bst = BinarySearchTree()
root = bst.insert(None, 50)
bst.insert(root, 30)

res = bst.search(root, 40)
print(res)
```

ก) 40
ข) None
ค) False
ง) Error

---

## ส่วนที่ 2: เฉลย

1. ก
2. ก
3. ค
4. ข
5. ก
6. ข
7. ค
8. ค
9. ข
10. ข
11. ค
12. ก
13. ค
14. ค
15. ค
16. ข
17. ก
18. ก
19. ง
20. ข

---

## หมายเหตุ

* Inorder (BST) → เรียงน้อย → มาก
* Preorder → Root → Left → Right
* Postorder → Left → Right → Root
* BFS → ไล่ระดับ (Level-order)
