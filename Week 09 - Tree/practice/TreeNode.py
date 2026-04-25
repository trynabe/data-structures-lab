class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level=0):
        print(" " * level * 4 + str(self.data))
        for child in self.children:
            child.print_tree(level + 1)

def build_family_tree():
    barcelona = TreeNode("Barcelona")
    cruyff = TreeNode("Cruyff")
    pep = TreeNode("Pep")
    barcelona.add_child(cruyff)
    barcelona.add_child(pep)

    hagi = TreeNode("Hagi")
    cruyff.add_child(hagi)
    koeman = TreeNode("Koeman")
    cruyff.add_child(koeman)

    xavi = TreeNode("Xavi")
    pep.add_child(xavi)
    iniesta = TreeNode("Iniesta")
    pep.add_child(iniesta)

    return barcelona

root = build_family_tree()
root.print_tree()