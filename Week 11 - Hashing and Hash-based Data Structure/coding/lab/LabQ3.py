import time

# ============================================================
# ใช้ HashTable จาก Lab 2 (ตัดข้อความ print ออกให้วัดเวลาได้)
# ============================================================

class HashTable:

    def __init__(self, M):
        self.M = M
        self.table = [None] * M
        self.collisions = 0       # นับ collision

    def _hash(self, key):
        total = 0
        for char in key.upper():
            total += ord(char)
        return total % self.M

    def put(self, key, value):
        slot = self._hash(key)

        if self.table[slot] is None:
            self.table[slot] = (key, value)

        elif self.table[slot][0] == key:
            self.table[slot] = (key, value)

        else:
            self.collisions += 1        # นับ collision
            i = 1
            while i < self.M:
                new_slot = (slot + i) % self.M
                if self.table[new_slot] is None:
                    self.table[new_slot] = (key, value)
                    break
                elif self.table[new_slot][0] == key:
                    self.table[new_slot] = (key, value)
                    break
                i += 1

    def get(self, key):
        slot = self._hash(key)
        for i in range(self.M):
            current = (slot + i) % self.M
            if self.table[current] is None:
                break
            if self.table[current][0] == key:
                return self.table[current][1]
        return None


# ============================================================
# ข้อมูล 20 รายการ
# ============================================================

data = [
    ("Ann",   "0810000001"), ("Bob",   "0810000002"),
    ("Cat",   "0810000003"), ("Dan",   "0810000004"),
    ("Eve",   "0810000005"), ("Fon",   "0810000006"),
    ("Gun",   "0810000007"), ("Han",   "0810000008"),
    ("Ivy",   "0810000009"), ("Jay",   "0810000010"),
    ("Kim",   "0810000011"), ("Lek",   "0810000012"),
    ("Mew",   "0810000013"), ("Non",   "0810000014"),
    ("Oak",   "0810000015"), ("Pam",   "0810000016"),
    ("Qin",   "0810000017"), ("Ray",   "0810000018"),
    ("Sam",   "0810000019"), ("Toy",   "0810000020"),
]

# ============================================================
# ทดสอบแต่ละขนาดตาราง
# ============================================================

sizes = [10, 20, 30, 40]

print("=" * 60)
print("Lab 3: Load Factor and Performance Analysis")
print("=" * 60)
print(f"{'Size (M)':<10} {'Load Factor':<14} {'Collision':<12} {'Insert Time':<15} {'Search Time'}")
print("-" * 60)

for M in sizes:

    ht = HashTable(M)

    # --- วัดเวลา Insert ---
    start = time.perf_counter()
    for key, value in data:
        ht.put(key, value)
    insert_time = time.perf_counter() - start

    # --- วัดเวลา Search (ค้นทุกคน) ---
    start = time.perf_counter()
    for key, value in data:
        ht.get(key)
    search_time = time.perf_counter() - start

    # --- คำนวณ Load Factor ---
    load_factor = len(data) / M

    print(f"{M:<10} {load_factor:<14.2f} {ht.collisions:<12} "
          f"{insert_time*1000:<15.4f} {search_time*1000:.4f}  (ms)")

print("-" * 60)
print("หน่วยเวลา: milliseconds (ms)")


# ============================================================
# อภิปรายผล
# ============================================================

print("\n" + "=" * 60)
print("อภิปรายผล")
print("=" * 60)
print("""
  M=10  Load=2.00 → ตารางเล็กเกินไป ข้อมูลล้นตาราง
                    ชนกันเยอะมาก ค้นหาช้า

  M=20  Load=1.00 → ตารางพอดีกับข้อมูล
                    ยังชนอยู่บ้าง

  M=30  Load=0.67 → ใกล้เคียง 0.7 ที่แนะนำ
                    ชนน้อยลง ค้นหาเร็วขึ้น

  M=40  Load=0.50 → ตารางใหญ่พอ
                    ชนน้อยที่สุด ค้นหาเร็วที่สุด

  สรุป: Load Factor ยิ่งต่ำ → Collision น้อย → ค้นหาเร็ว
        แต่ใช้ Memory มากขึ้น
        ค่าที่เหมาะสมคือประมาณ 0.7
""")