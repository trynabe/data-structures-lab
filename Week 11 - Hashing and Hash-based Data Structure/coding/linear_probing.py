class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        # สร้างตารางแฮชโดยกำหนดค่าเริ่มต้นเป็น None (ช่องว่าง) ตามขนาด
        self.table = [None] * size

    def hash_function(self, key):
        # ฟังก์ชันแฮช h(k) = k % 7 ตามที่ระบุในสไลด์
        return key % self.size

    def insert(self, key):
        # 1. คำนวณหาตำแหน่งเริ่มต้น (h(k))
        initial_index = self.hash_function(key)
        index = initial_index
        step = 0
        
        print(f"Trying to insert {key}... (h({key}) = {initial_index})")

        # 2. ถ้าช่องที่คำนวณได้ไม่ว่าง (มีข้อมูลอยู่แล้ว) ให้ขยับหาช่องถัดไป
        while self.table[index] is not None:
            print(f"  -> Collision at index {index}! Moving to next slot...")
            step += 1
            # คำนวณตำแหน่งใหม่ (h(k) + step) % 7
            index = (initial_index + step) % self.size
            
            # ป้องกันการวนลูปไม่รู้จบกรณีตารางเต็ม
            if step == self.size:
                print(f"  -> Hash table is full! Cannot insert {key}.")
                return

        # 3. เจอช่องว่างแล้ว ทำการจัดเก็บข้อมูล
        self.table[index] = key
        print(f"  -> Successfully inserted {key} at index {index}\n")

    def display(self):
        print("--- Final Hash Table Structure ---")
        for i in range(self.size):
            print(f"Index {i}: [{self.table[i]}]")

# ขนาดตารางตามรูปคือ 7 (มี index 0 ถึง 6)
ht = LinearProbingHashTable(7)

# แทรกข้อมูลตามลำดับในสไลด์: 12, 19, 33, 20
data = [12, 19, 33, 20]

print("--- Starting Linear Probing Insertion ---\n")
for num in data:
    ht.insert(num)

ht.display()
