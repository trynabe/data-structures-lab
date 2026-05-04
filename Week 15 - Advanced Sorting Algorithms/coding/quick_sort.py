def quick_sort(arr):
    print(f"input: {arr}")
    result = _quick_sort(arr[:])
    print(f"output: {arr}")
    return result

def _quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return _quick_sort(left) + [pivot] + _quick_sort(right)

sample_list0 = [85, 24, 63, 45, 17, 31, 96, 50]
sample_list1 = [45, 23, 87, 12, 32, 4, 54, 32, 52]
sample_list2 = [94, 58, 79, 55, 95, 32, 46, 90, 76, 13]
# sample_list3 = [1,2,3,4,5,99,98,97,96,95,30,31,32,33,34,
#                 55,56,57,58,59,88,86,84,82,80,77,75,73,71,69,
#                 44,46,48,50,52,17,18,19,20,21,29,28,27,26,25,
#                 6,7,8,9,10]

for lst in [sample_list0, sample_list1, sample_list2]:
    quick_sort(lst)