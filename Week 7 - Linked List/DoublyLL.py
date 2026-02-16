# Node Representation in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

# Inserting at the Head
    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

# Inserting at the Tail
    def add_last(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

# Removing a Specific Node
    def remove_node(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if temp is None:
            return
        if temp == self.head:
            self.remove_first()
        elif temp == self.tail:
            self.remove_last()
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.size -= 1

# Removing the Head Node
    def remove_first(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
    
# Removing the Tail Node
    def remove_last(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

# Traversing a Doubly Linked List
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("NULL")
    
    def traverse_backward(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" <- ")
            temp = temp.prev
        print("NULL")
        