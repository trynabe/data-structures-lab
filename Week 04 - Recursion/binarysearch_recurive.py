# Binary Search Algorithm (Recursive Code)

# Example Input arr : 1 3 5 7 9 11 13
data = list(map(int, input("Enter sorted numbers (space-separated): ").split()))
# Example Input target : 7
target = int(input("Enter target number: "))

def binary_search(data, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)
    
data.sort()

data.sort()

result = binary_search(data, target, 0, len(data) - 1)

if result != -1:
    print("Found at index:", result)
else:
    print("Not found")