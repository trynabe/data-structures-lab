from circular_deque import CircularDeque

def main():
    # Create a CircularDeque with a default capacity of 10
    deque = CircularDeque()

    # Test add_first and add_last operations
    deque.add_first(10)
    deque.add_last(20)
    deque.add_first(5)
    deque.add_last(30)
    print("Deque after adding elements:", [deque._data[i] for i in range(len(deque._data))])

    # Test first and last methods
    print("First element:", deque.first())
    print("Last element:", deque.last())

    # Test delete_first and delete_last operations
    print("Removed first element:", deque.delete_first())
    print("Removed last element:", deque.delete_last())

    # Test the state of the deque
    print("Deque after removals:", [deque._data[i] for i in range(len(deque._data))])
    print("Deque size:", len(deque))

    # Test resizing
    print("\nTesting resizing:")
    for i in range(15):
        deque.add_last(i)
    print("Deque after adding 15 elements:", [deque._data[i] for i in range(len(deque._data))])
    print("Deque size after resizing:", len(deque))

if __name__ == "__main__":
    main()