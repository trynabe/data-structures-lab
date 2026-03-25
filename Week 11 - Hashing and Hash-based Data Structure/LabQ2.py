# ============================================================
# Lab 2: Hash Table เก็บชื่อเล่น + เบอร์โทร
# ============================================================

class SimpleHashTable:

    # สร้างตารางขนาด M ช่อง
    def __init__(self, M=10):
        self.M = M
        self.table = [None] * M   # [None, None, None, ...]

    # แปลงชื่อเป็นตัวเลข
    def _hash(self, key):
        total = 0
        for char in key.upper():
            total += ord(char)
        return total % self.M

    # ใส่ข้อมูล
    def put(self, key, value):
        slot = self._hash(key)

        # ถ้าช่องว่าง → เก็บเลย
        if self.table[slot] is None:
            self.table[slot] = (key, value)
            print(f"  เก็บ ({key}, {value}) → slot {slot}")

        # ถ้า key ซ้ำ → update
        elif self.table[slot][0] == key:
            self.table[slot] = (key, value)
            print(f"  update ({key}, {value}) → slot {slot}")

        # ถ้าชนกัน → Linear Probing หาช่องว่างถัดไป
        else:
            print(f"  Collision! {key} ชนกับ {self.table[slot][0]} ที่ slot {slot}")
            i = 1
            while i < self.M:
                new_slot = (slot + i) % self.M
                if self.table[new_slot] is None:
                    self.table[new_slot] = (key, value)
                    print(f"  เก็บ ({key}, {value}) → slot {new_slot} แทน")
                    break
                elif self.table[new_slot][0] == key:
                    self.table[new_slot] = (key, value)
                    print(f"  update ({key}, {value}) → slot {new_slot}")
                    break
                i += 1

    # ค้นหาข้อมูล
    def get(self, key):
        slot = self._hash(key)

        # วนหาตั้งแต่ slot เดิม
        for i in range(self.M):
            current = (slot + i) % self.M
            if self.table[current] is None:
                break
            if self.table[current][0] == key:
                return self.table[current][1]   # คืนค่าเบอร์

        return None   # ไม่เจอ

    # ลบข้อมูล
    def remove(self, key):
        slot = self._hash(key)

        for i in range(self.M):
            current = (slot + i) % self.M
            if self.table[current] is None:
                break
            if self.table[current][0] == key:
                self.table[current] = None
                print(f"  ลบ {key} ออกจาก slot {current}")
                return

        print(f"  ไม่พบ {key}")

    # แสดงตาราง
    def display(self):
        print("\n  Slot | Data")
        print("  " + "-" * 30)
        for i, item in enumerate(self.table):
            print(f"  {i:>4} | {item}")


# ============================================================
# ทดสอบ
# ============================================================

ht = SimpleHashTable(M=10)

print("=" * 40)
print("ใส่ข้อมูลปกติ")
print("=" * 40)
ht.put("Ann",  "0812345678")
ht.put("Bob",  "0823456789")
ht.put("Eve",  "0834567890")

print("\n" + "=" * 40)
print("ทดสอบ Collision (Ann กับ Nna มี ASCII เท่ากัน)")
print("=" * 40)
ht.put("Nna",  "0899999999")   # ← ชนกับ Ann แน่นอน

print("\n" + "=" * 40)
print("ทดสอบ update (ใส่ Ann ซ้ำ)")
print("=" * 40)
ht.put("Ann",  "0800000000")   # ← update เบอร์ใหม่

print("\n" + "=" * 40)
print("ค้นหาข้อมูล")
print("=" * 40)
print(f"  หา Ann  → {ht.get('Ann')}")
print(f"  หา Bob  → {ht.get('Bob')}")
print(f"  หา Zzz  → {ht.get('Zzz')}")   # ไม่มีในตาราง

print("\n" + "=" * 40)
print("ลบข้อมูล")
print("=" * 40)
ht.remove("Bob")
ht.remove("Zzz")   # ไม่มีในตาราง

ht.display()