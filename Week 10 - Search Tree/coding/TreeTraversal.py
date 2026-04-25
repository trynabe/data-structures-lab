from collections import deque

# ── create tree ──────────────────────────────────────
#         A
#        / \
#       B   C
#      / \   \
#     D   E   F

class Node:
    def __init__(self, val, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

root = Node("A",
        Node("B", Node("D"), Node("E")),
        Node("C", Node("F")))

# ── Traversal functions ───────────────────────────────────

def preorder(node):
    """Root → Left → Right"""
    if node:
        print(node.val, end=" → ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    """Left → Root → Right"""
    if node:
        inorder(node.left)
        print(node.val, end=" → ")
        inorder(node.right)

def postorder(node):
    """Left → Right → Root"""
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=" → ")

def bfs(root):
    """Level-order (ทีละชั้น) ใช้ queue"""
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" → ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# ── Output ────────────────────────────────────────────────

print("Preorder  (Root→L→R):", end=" ")
preorder(root)
print("end")

print("Inorder   (L→Root→R):", end=" ")
inorder(root)
print("end")

print("Postorder (L→R→Root):", end=" ")
postorder(root)
print("end")

print("BFS       (Floors):", end=" ")
bfs(root)
print("end")