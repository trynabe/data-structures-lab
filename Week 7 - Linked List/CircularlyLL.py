# Node Representation in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Linked List Class
class CircularLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

# Inserting at the Head
    def add_first(self, data):
        new_node = Node(data)
        if self.tail is None:
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
        self.size += 1

# Inserting at the Tail
    def add_last(self, data):
        new_node = Node(data)
        if self.tail is None:
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

# Removing the Head Node
    def remove_first(self):
        if self.tail is None:
            return
        if self.tail.next == self.tail:
            self.tail = None
        else:
            self.tail.next = self.tail.next.next
        self.size -= 1

# Traversing a Circular Linked List
    def traverse(self):
        if self.tail is None:
            return
        temp = self.tail.next
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.tail.next:
                break
        print("(back to head)")