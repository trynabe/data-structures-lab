# circular_deque.py

class CircularDeque:
    """Circular Deque implementation using a Python list as underlying storage."""

    def __init__(self, capacity=10):
        """Create an empty deque with a fixed capacity."""
        self._data = [None] * capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size

    def is_empty(self):
        """Return True if the deque is empty."""
        return self._size == 0

    def add_first(self, e):
        """Add an element to the front of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Add an element to the back of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        """Remove and return the first element of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")
        result = self._data[self._front]
        self._data[self._front] = None # Help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return result

    def delete_last(self):
        """Remove and return the last element of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        result = self._data[back]
        self._data[back] = None # Help garbage collection
        self._size -= 1
        return result

    def first(self):
        """Return (but do not remove) the first element of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the last element of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def _resize(self, capacity):
        """Resize to a new list of capacity >= len(self)."""
        old_data = self._data
        self._data = [None] * capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old_data[walk]
            walk = (walk + 1) % len(old_data)
        self._front = 0