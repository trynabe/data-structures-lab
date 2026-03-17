class LinkedTree:
    class _Node:
        __slots__ = '_element', '_parent', '_children'

        def __init__(self, element, parent=None):
            self._element = element
            self._parent = parent
            self._children = []

    def __init__(self):
        self._root = None
        self._size = 0

    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root already exists')
        self._root = self._Node(e)
        self._size = 1 
        return self._root
    
    def add_child(self, p, e):
        new_node = self._Node(e, p)
        p._children.append(new_node)
        self._size += 1
        return new_node
    
    def display(self, node, level=0):
        # Professional tree display with indentation
        indent = "    " * level
        marker = "|-- " if level > 0 else ""
        print(f"{indent}{marker}{node._element}")
        for child in node._children:
            self.display(child, level + 1)

# --- Start Program Execution ---
tree = LinkedTree()

# 1. Create the Root node for Thailand National Team (Zico Era)
root = tree.add_root("Thailand National Team (Zico Era)")

# 2. Add Coaching Staff info
tree.add_child(root, "Head Coach: Kiatisuk Senamuang")

# 3. Best XI organized by Positions
# --- Goalkeeper ---
gk = tree.add_child(root, "Goalkeeper")
tree.add_child(gk, "Kawin Thamsatchanan (SENSE)")

# --- Defenders ---
df = tree.add_child(root, "Defenders (Back 4)")
tree.add_child(df, "RB: Narubadin Weerawatnodom")
tree.add_child(df, "CB: Tanaboon Kesarat")
tree.add_child(df, "CB: Suttinan Phuk-hom")
tree.add_child(df, "LB: Theeraton Bunmathan (Captain)")

# --- Midfielders ---
mf = tree.add_child(root, "Midfielders (The Engine)")
tree.add_child(mf, "DMF: Sarach Yooyen")
tree.add_child(mf, "CMF: Charyl Chappuis")
tree.add_child(mf, "AMF: Chanathip Songkrasin (Messi Jay)")

# --- Forwards ---
fw = tree.add_child(root, "Forwards (The Attackers)")
tree.add_child(fw, "RW: Mongkol Tossakrai")
tree.add_child(fw, "LW: Kroekrit Thaweekarn")
tree.add_child(fw, "CF: Teerasil Dangda")

# 3. Display the structure
print("=== Structure: Thailand Best XI (Zico Era) ===")
tree.display(root)
print(f"\nTotal Nodes in Tree: {tree._size}")