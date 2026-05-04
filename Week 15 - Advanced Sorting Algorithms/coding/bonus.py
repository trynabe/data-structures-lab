import numpy as np
import timeit
import sys
sys.setrecursionlimit(100000)

# Merge Sort (จาก Lab 1 แต่ไม่ print)
def merge_sort_silent(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_silent(arr[:mid])
    right = merge_sort_silent(arr[mid:])
    return merge_silent(left, right)

def merge_silent(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort (จาก Lab 2 แต่ไม่ print)
def quick_sort_silent(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]   # ใช้ตรงกลางเพื่อหลีกเลี่ยง worst case
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_silent(left) + mid + quick_sort_silent(right)

print(f"{'ชุดข้อมูล':<20} {'Merge Sort (วินาที)':<25} {'Quick Sort (วินาที)'}")

# สร้างชุดข้อมูล
sizes = [10, 100, 1000, 5000, 10000, 20000]
datasets = {n: np.random.randint(0, n * 10, n).tolist() for n in sizes}

for n in sizes:
    data = datasets[n]

    start = timeit.default_timer()
    merge_sort_silent(data[:])
    merge_time = timeit.default_timer() - start

    start = timeit.default_timer()
    quick_sort_silent(data[:])
    quick_time = timeit.default_timer() - start

    print(f"จำนวน {n:<14} {merge_time:<25.6f} {quick_time:.6f}")