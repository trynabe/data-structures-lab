# ===== NODE CLASS =====
class Node:
    def __init__(self, element, parent=None):
        self._element = element
        self._parent = parent
        self._children = []

    def element(self):
        return self._element


# ===== LINKED TREE CLASS =====
class LinkedTree:
    def __init__(self):
        self._root = None

    def root(self):
        """Return the root node."""
        return self._root

    def add_child(self, parent, element):
        """Add a new child node under the given parent."""
        new_node = Node(element, parent)
        if parent is None:
            self._root = new_node   # No parent = this is the root
        else:
            parent._children.append(new_node)
        return new_node

    def children(self, node):
        """Return an iterator of a node's children."""
        return iter(node._children)

    def num_children(self, node):
        """Return the number of children a node has."""
        return len(node._children)

    def parent(self, node):
        """Return the parent of a node."""
        return node._parent

    def remove(self, node):
        """Remove a node and all its descendants."""
        if node._parent is not None:
            node._parent._children.remove(node)
            node._parent = None

    def find_element(self, target):
        """Search for a node by element value. Returns None if not found."""
        return self._find_recursive(self._root, target)

    def _find_recursive(self, node, target):
        """Helper: recursively search the tree."""
        if node is None:
            return None
        if node.element() == target:
            return node
        for child in node._children:
            result = self._find_recursive(child, target)
            if result is not None:
                return result
        return None

# ===== SAMPLE TREE SETUP =====
def create_sample_tree():
    tree = LinkedTree()
    root = tree.add_child(None, "Root")
    child1 = tree.add_child(root, "Child 1")
    child2 = tree.add_child(root, "Child 2")
    subchild1 = tree.add_child(child1, "Subchild 1")
    subchild2 = tree.add_child(child1, "Subchild 2")
    return tree

# ===== TEST 1: Validate Tree Structure =====
def test_tree_structure():
    tree = create_sample_tree()
    assert tree.root().element() == "Root"
    assert tree.num_children(tree.root()) == 2
    assert tree.num_children(next(tree.children(tree.root()))) == 2
    print("Tree structure test passed.")

# ===== TEST 2: Validate Parent-Child Relationships =====
def test_parent_references():
    tree = create_sample_tree()
    root = tree.root()
    child1 = next(tree.children(root))
    assert tree.parent(child1).element() == root.element(), \
        f"Expected parent: {root.element()}, Got: {tree.parent(child1).element()}"
    print("Parent reference test passed.")

# ===== TEST 3: Test Adding a New Node =====
def test_add_child():
    tree = create_sample_tree()
    root = tree.root()
    new_child = tree.add_child(root, "New Child")
    assert tree.num_children(root) == 3
    assert new_child.element() == "New Child"
    print("Add child test passed.")

# ===== TEST 4: Test Removing a Node =====
def test_remove():
    tree = create_sample_tree()
    child1 = next(tree.children(tree.root()))  # Get the first child
    tree.remove(child1)  # Remove the node
    assert tree.num_children(tree.root()) == 1, "Child removal failed."
    print("Remove test passed.")

# ===== TEST 5: Test Searching for Elements =====
def test_find_element():
    tree = create_sample_tree()
    root = tree.root()
    child1 = next(tree.children(root))
    subchild1 = next(tree.children(child1))

    # Should find existing nodes correctly
    assert tree.find_element("Child 1").element() == child1.element(), "Error: 'Child 1' not found."
    assert tree.find_element("Subchild 1").element() == subchild1.element(), "Error: 'Subchild 1' not found."

    # Should return None for non-existent nodes
    assert tree.find_element("Nonexistent") is None, "Error: Found non-existent element."
    print("Find element test passed.")

# ===== RUN ALL TESTS =====
def run_tests():
    test_tree_structure()
    test_parent_references()
    test_add_child()
    test_remove()
    test_find_element()
    print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()

# Root
# ├── Child 1
# │   ├── Subchild 1
# │   └── Subchild 2
# └── Child 2
