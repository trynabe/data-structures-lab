# ============================================================
# Lab 1: Hash Function - ทั้ง 4 Task
# ============================================================

# ============================================================
# Task 1: แปลงชื่อเป็นตัวเลข (Adding Digits / ASCII)
# ============================================================

def string_to_number(name):
    total = 0
    for char in name.upper():
        total += ord(char)
    return total

print("=" * 50)
print("Task 1: แปลงชื่อเป็นตัวเลข")
print("=" * 50)
names = ["ANT", "BAT", "CAT", "DOG", "ICT", "DST", "LUV"]
for name in names:
    print(f"  {name} → {string_to_number(name)}")


# ============================================================
# Task 2: Hash Function แบบ Modulo
# ============================================================

def hash_modulo(name, M=10):
    k = string_to_number(name)
    return k % M

print("\n" + "=" * 50)
print("Task 2: Modulo Method (M=10)")
print("=" * 50)
for name in names:
    print(f"  {name} → slot {hash_modulo(name)}")


# ============================================================
# Task 3: เปลี่ยนเป็นวิธีอื่น (Digit Folding, Mid-Square, Multiplication)
# ============================================================

def hash_digit_folding(name, M=10, r=2):
    k = str(string_to_number(name))
    total = 0
    for i in range(0, len(k), r):
        part = k[i:i+r]
        total += int(part)
    result = int(str(total)[-r:]) % M
    return result

def hash_mid_square(name, M=10, r=2):
    k = string_to_number(name)
    squared = str(k * k)
    mid = len(squared) // 2
    half = r // 2
    middle_digits = squared[mid - half : mid + half]
    if not middle_digits:
        middle_digits = squared[:r]
    return int(middle_digits) % M

def hash_multiplication(name, M=10, A=0.357840):
    k = string_to_number(name)
    return int(M * ((k * A) % 1))

print("\n" + "=" * 50)
print("Task 3: วิธีอื่นๆ (M=10)")
print("=" * 50)
for name in names:
    print(f"  {name} → Folding={hash_digit_folding(name)}  "
          f"MidSquare={hash_mid_square(name)}  "
          f"Multiply={hash_multiplication(name)}")


# ============================================================
# Task 4: เปรียบเทียบประสิทธิภาพ (นับการชนกัน)
# ============================================================

def count_collisions(hash_func, names, M=10):
    table = {}
    collisions = 0
    for name in names:
        slot = hash_func(name, M)
        if slot in table:
            collisions += 1
        else:
            table[slot] = name
    return collisions

print("\n" + "=" * 50)
print("Task 4: เปรียบเทียบจำนวน Collision (M=10)")
print("=" * 50)
methods = {
    "Modulo":       hash_modulo,
    "Digit Folding": hash_digit_folding,
    "Mid-Square":   hash_mid_square,
    "Multiplication": hash_multiplication,
}

for method_name, func in methods.items():
    c = count_collisions(func, names)
    print(f"  {method_name:<18} → collision = {c} ครั้ง")

print("\n" + "=" * 50)
print("สรุปตารางเปรียบเทียบทุกวิธี")
print("=" * 50)
print(f"{'Name':<8} {'ASCII':>6} {'Modulo':>8} {'Folding':>8} {'MidSq':>8} {'Multiply':>9}")
print("-" * 50)
for name in names:
    print(f"{name:<8} "
          f"{string_to_number(name):>6} "
          f"{hash_modulo(name):>8} "
          f"{hash_digit_folding(name):>8} "
          f"{hash_mid_square(name):>8} "
          f"{hash_multiplication(name):>9}")