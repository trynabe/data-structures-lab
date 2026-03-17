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
        # Format the display to visualize the tree structure
        indent = "    " * level
        marker = "|--> " if level > 0 else ""
        print(f"{indent}{marker}{node._element}")
        for child in node._children:
            self.display(child, level + 1)

# --- Start Program Execution ---
tree = LinkedTree()

# 1. Create the Root node
root = tree.add_root("World Cup 2026")

# 2. Add Teams with Captains and Full Starting XI
# --- ARGENTINA ---
arg = tree.add_child(root, "Argentina")
tree.add_child(arg, "Captain: Lionel Messi")
arg_xi = tree.add_child(arg, "Starting XI (4-3-3)")
for player in ["E. Martínez", "Molina", "Romero", "Otamendi", "Tagliafico", 
               "De Paul", "Enzo Fernández", "Mac Allister", 
               "Lionel Messi", "Julián Álvarez", "Angel Di María"]:
    tree.add_child(arg_xi, player)

# --- PORTUGAL ---
por = tree.add_child(root, "Portugal")
tree.add_child(por, "Captain: Cristiano Ronaldo")
por_xi = tree.add_child(por, "Starting XI (4-3-3)")
for player in ["Diogo Costa", "Cancelo", "Ruben Dias", "Pepe", "Nuno Mendes", 
               "Palhinha", "Bruno Fernandes", "Vitinha", 
               "Bernardo Silva", "Cristiano Ronaldo", "Rafael Leão"]:
    tree.add_child(por_xi, player)

# --- ENGLAND ---
eng = tree.add_child(root, "England")
tree.add_child(eng, "Captain: Harry Kane")
eng_xi = tree.add_child(eng, "Starting XI (4-2-3-1)")
for player in ["Pickford", "Walker", "Stones", "Guehi", "Trippier", 
               "Rice", "Mainoo", "Saka", "Bellingham", "Foden", "Harry Kane"]:
    tree.add_child(eng_xi, player)

# --- BRAZIL ---
bra = tree.add_child(root, "Brazil")
tree.add_child(bra, "Captain: Marquinhos")
bra_xi = tree.add_child(bra, "Starting XI (4-2-3-1)")
for player in ["Alisson", "Danilo", "Marquinhos", "Gabriel Magalhães", "Arana", 
               "Bruno Guimarães", "João Gomes", "Raphinha", "Lucas Paquetá", "Vinícius Júnior", "Rodrygo"]:
    tree.add_child(bra_xi, player)

# --- FRANCE ---
fra = tree.add_child(root, "France")
tree.add_child(fra, "Captain: Kylian Mbappé")
fra_xi = tree.add_child(fra, "Starting XI (4-3-3)")
for player in ["Maignan", "Koundé", "Upamecano", "Saliba", "Theo Hernández", 
               "Tchouaméni", "Kanté", "Rabiot", "Dembélé", "Griezmann", "Kylian Mbappé"]:
    tree.add_child(fra_xi, player)

# 3. Display the entire structure
print("=== World Cup 2026: Full Squad Hierarchical Structure ===")
tree.display(root)
print(f"\nTotal Nodes (Nodes/Players/Categories): {tree._size}")