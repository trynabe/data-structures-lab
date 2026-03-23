class LinkedTree:

    class _Node:
        __slots__ = '_element', '_parent', '_children'
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
        def __repr__(self):
            return f"Position({self._node._element})"

    def _validate(self, p):
        """Return the node associated with Position p."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):       return self._size
    def root(self):          return self._make_position(self._root)
    def is_root(self, p):    return self.root() == p
    def is_leaf(self, p):    return self.num_children(p) == 0

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def children(self, p):
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    def num_children(self, p):
        node = self._validate(p)
        return len(node._children)

    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_child(self, p, e):
        node  = self._validate(p)
        self._size += 1
        child = self._Node(e, node)
        node._children.append(child)
        return self._make_position(child)

    def delete(self, p):
        node = self._validate(p)
        if node._children:
            raise ValueError('Cannot delete node with children')
        parent = node._parent
        if parent is None:
            self._root = None
        else:
            parent._children.remove(node)
        self._size -= 1
        node._parent = node  # mark deprecated
        return node._element

    def depth(self, p):
        if self.is_root(p): return 0
        return 1 + self.depth(self.parent(p))

    def _print_tree(self, p, indent=0):
        prefix = '  ' * indent + ('└─ ' if indent > 0 else '')
        print(prefix + p.element())
        for child in self.children(p):
            self._print_tree(child, indent + 1)

    def print_tree(self):
        if self.root() is None:
            print("(empty tree)")
        else:
            self._print_tree(self.root())


# ══════════════════════════════════════════════════════
#  DEMO — FIFA World Cup 2026
# ══════════════════════════════════════════════════════
print("=" * 55)
print("  🏆 FIFA World Cup 2026 — LinkedTree Demo")
print("=" * 55)

t = LinkedTree()

# Root
wc = t.add_root("🏆 FIFA World Cup 2026")

# Groups (ชั้น 1)
group_a = t.add_child(wc, "📌 Group A")
group_b = t.add_child(wc, "📌 Group B")
group_c = t.add_child(wc, "📌 Group C")

# Teams in Group A
brazil  = t.add_child(group_a, "🇧🇷 Brazil")
germany = t.add_child(group_a, "🇩🇪 Germany")
japan   = t.add_child(group_a, "🇯🇵 Japan")

# Teams in Group B
france    = t.add_child(group_b, "🇫🇷 France")
argentina = t.add_child(group_b, "🇦🇷 Argentina")
mexico    = t.add_child(group_b, "🇲🇽 Mexico")

# Teams in Group C
spain    = t.add_child(group_c, "🇪🇸 Spain")
thailand = t.add_child(group_c, "🇹🇭 Thailand")
usa      = t.add_child(group_c, "🇺🇸 USA")

print(f"\nTotal nodes in tree: {len(t)}")

print("\n" + "=" * 55)
print("  🌳 Structure Tree")
print("=" * 55)
t.print_tree()

print("\n" + "=" * 55)
print("  ✅ Tester _validate(p)")
print("=" * 55)
print(f"validate(brazil)  → node = {t._validate(brazil)._element}")
print(f"validate(france)  → node = {t._validate(france)._element}")
print(f"validate(wc)      → node = {t._validate(wc)._element}")

print("\n--- ❌ Error Cases ---")

# TypeError
try:
    t._validate("Group A")
except TypeError as e:
    print(f"TypeError  ✓ : {e}")

# ValueError: wrong container
t2 = LinkedTree()
other = t2.add_root("⚽ Other Tournament")
try:
    t._validate(other)
except ValueError as e:
    print(f"ValueError ✓ : {e}")

# ValueError: deprecated node
print(f"\nลบ 🇹🇭 Thailand Left Group C...")
t.delete(thailand)
try:
    t._validate(thailand)
except ValueError as e:
    print(f"ValueError ✓ : {e}")

print("\n" + "=" * 55)
print("  🔧 Tester _make_position(node)")
print("=" * 55)
brazil_node = t._validate(brazil)
pos = t._make_position(brazil_node)
print(f"_make_position(brazil_node) → {pos}")
print(f"_make_position(None)        → {t._make_position(None)}")

print("\n" + "=" * 55)
print("  📊 Information Node")
print("=" * 55)
print(f"{'Node':<25} | depth | children | is_leaf")
print("-" * 55)
for p in [wc, group_a, group_b, group_c, brazil, france, spain, usa]:
    print(f"{p.element():<25} |   {t.depth(p)}   |    {t.num_children(p)}     |  {t.is_leaf(p)}")

print("\n" + "=" * 55)
print("  🌳 Tree Del. Thailand")
print("=" * 55)
t.print_tree()