def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

numbers = [725, 442, 329, 121, 552, 682]

print("Selection Sort")
print("Before:", numbers)
sorted_numbers = insertion_sort(numbers.copy())
print("After :", sorted_numbers)