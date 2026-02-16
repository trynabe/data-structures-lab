# Node Representation in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating a Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

# Inserting at the Head
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

# Inserting at the Tail
    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

# Removing the Head Node
    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1

# Removing from the tail 
    def remove_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.size -= 1

# Remove a Specific Node
    def remove_node(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            self.remove_first()
            return
        temp = self.head
        while temp.next and temp.next.data != key:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next
            if temp.next is None:
                self.tail = temp
            self.size -= 1

# Traversing the List
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

# Finding an Element
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False