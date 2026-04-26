class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def _hash_function(self, key):
        return key % self.size
    
    def insert(self, key):
        index = self._hash_function(key)
        self.table[index] = key
        print(f"Inserting key {key} at index {index}")
    
    def search(self, key):
        index = self._hash_function(key)
        if self.table[index] == key:
            return index
        return None
    
my_hash = SimpleHashTable(size=100)
number = [10, 20, 30, 40, 50, 60]

for n in number:
    my_hash.insert(n)

target = 40
result_index = my_hash.search(target)

if result_index is not None:
    print(f"Key {target} found at index {result_index}")
else:
    print(f"Key {target} not found")