# Binary Search Algorithm (Iterative Code)

# Example Input arr : 1 3 5 7 9 11 13
arr = list(map(int, input("Enter sorted numbers (space-separated) : ").split()))
# Example Input target : 7
target = int(input("Enter target number : "))

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

result = binary_search(arr, target)

if result != -1:
    print("Found at index :", result)
else:
    print("Not found")