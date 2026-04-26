class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        # สร้างตารางแฮชโดยกำหนดค่าเริ่มต้นเป็น None (ช่องว่าง)
        self.table = [None] * size

    def h1(self, key):
        # ฟังก์ชันแฮชหลัก h1(k) = k % 7
        return key % self.size

    def h2(self, key):
        # ฟังก์ชันแฮชสำรอง h2(k) = 1 + (k % 7)
        return 1 + (key % 7)

    def insert(self, key):
        initial_index = self.h1(key)
        index = initial_index
        j = 0  # j คือ จำนวนครั้งที่เกิดการชนกัน [cite: 539]
        
        print(f"Trying to insert {key}... (h1({key}) = {initial_index})")

        # ถ้าช่องที่คำนวณได้ไม่ว่าง (มีข้อมูลอยู่แล้ว)
        while self.table[index] is not None:
            print(f"  -> Collision at index {index}! Calculating new slot...")
            j += 1
            step_size = self.h2(key)
            
            # สูตรคำนวณตำแหน่งใหม่: h(k, j) = (h1(k) + j*h2(k)) % 7 
            index = (initial_index + (j * step_size)) % self.size
            print(f"     Step {j}: (h1 + {j} * h2) % {self.size} = ({initial_index} + {j} * {step_size}) % {self.size} = {index}")
            
            # ดักไว้ป้องกันการวนลูปไม่รู้จบ
            if j == self.size:
                print(f"  -> Could not find a valid slot for {key}.")
                return

        # เจอช่องว่างแล้ว ทำการจัดเก็บข้อมูล
        self.table[index] = key
        print(f"  -> Successfully inserted {key} at index {index}\n")

    def display(self):
        print("--- Final Hash Table Structure ---")
        for i in range(self.size):
            print(f"Index {i}: [{self.table[i]}]")

# ขนาดตารางตามรูปคือ 7
ht = DoubleHashingHashTable(7)

# แทรกข้อมูลตามลำดับ: 12, 19, 33, 20
data = [12, 19, 33, 20]

print("--- Starting Double Hashing Insertion ---\n")
for num in data:
    ht.insert(num)

ht.display()