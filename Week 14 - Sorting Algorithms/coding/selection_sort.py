def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

numbers = [25, 22, 29, 12, 52, 62]

print("Selection Sort")
print("Before:", numbers)
sorted_numbers = selection_sort(numbers.copy())
print("After :", sorted_numbers)