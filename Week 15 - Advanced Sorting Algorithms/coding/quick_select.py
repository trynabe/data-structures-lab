import random
import timeit

def randomized_quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)

    low = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]

    if k <= len(low):
        return randomized_quick_select(low, k)
    elif k <= len(low) + len(mid):
        return pivot
    else:
        return randomized_quick_select(high, k - len(low) - len(mid))
    
def print_ranks(arr, k_start, k_end):
    print(f"input: {arr}")
    for k in range(k_start, k_end + 1):
        result = randomized_quick_select(arr[:], k)
        print(f"Rank #{k:2} : {result}")
    print()

# ==================== ข้อ 1: ทดสอบพื้นฐาน ====================
S = [55, 29, 32, 43, 43, 9, 19, 90, 76, 13, 43, 29, 65, 88, 76]

print_ranks(S, 1, 10)

# ==================== ข้อ 2: วัดประสิทธิผลเมื่อปรับ k ====================
print("วัดเวลาเฉลี่ยเมื่อปรับค่า k (รัน 1000 ครั้งต่อค่า k)")
print(f"{'k':<6} {'เวลาเฉลี่ย (วินาที)'}")

test_arr = [random.randint(0, 1000) for _ in range(100)]
n = len(test_arr)

for k in [1, 25, 50, 75, 100]:
    total = 0
    runs = 1000
    for _ in range(runs):
        start = timeit.default_timer()
        randomized_quick_select(test_arr[:], k)
        total += timeit.default_timer() - start
    avg = total / runs
    print(f"{k:<6} {avg:.8f}")
print()

# ==================== ข้อ 3: ทดสอบหลายชุด ====================
print("ทดสอบหลายชุดข้อมูล")

datasets = [
    [85, 24, 63, 45, 17, 31, 96, 50],
    [45, 23, 87, 12, 32, 4, 54, 32, 52],
    [94, 58, 79, 55, 95, 32, 46, 90, 76, 13],
    [1, 1, 1, 1, 5, 5, 5, 9, 9, 9],   # มีค่าซ้ำเยอะ
]

for i, data in enumerate(datasets):
    print(f"\nชุดที่ {i+1}: {data}")
    mid_k = len(data) // 2
    result = randomized_quick_select(data[:], mid_k)
    expected = sorted(data)[mid_k - 1]
    print(f"  Rank #{mid_k} = {result}  (ตรวจสอบ: {expected}) {'✓' if result == expected else '✗'}")