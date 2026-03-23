# circular_queue.py

class CircularQueue:
    """Circular Queue implementation using a Python list as underlying storage."""

    def __init__(self, capacity):
        """Create an empty queue with a fixed capacity."""
        self._data = [None] * capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        if self._size == len(self._data):
            raise Exception('Queue is full')
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if self.is_empty():
            raise Exception('Queue is empty')
        result = self._data[self._front]
        self._data[self._front] = None # Help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return result

    def first(self):
        """Return (but do not remove) the front element of the queue."""
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]