sample_list0 = [85, 24, 63, 45, 17, 31, 96, 50]
sample_list1 = [45, 23, 87, 12, 32, 4, 54, 32, 52]
sample_list2 = [94, 58, 79, 55, 95, 32, 46, 90, 76, 13]
# sample_list3 = [1,2,3,4,5,99,98,97,96,95,30,31,32,33,34,
#                 55,56,57,58,59,88,86,84,82,80,77,75,73,71,69,
#                 44,46,48,50,52,17,18,19,20,21,29,28,27,26,25,
#                 6,7,8,9,10]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    print(f"devide: {arr} into {left} and {right}")

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    print(f"combine: {left} and {right} to {result}")
    return result

for i, lst in enumerate([sample_list0, sample_list1, sample_list2]):
    print(f"sample list{i}: {lst}")
    result = merge_sort(lst)
    print(f"Merge Sort (final result): {result}")