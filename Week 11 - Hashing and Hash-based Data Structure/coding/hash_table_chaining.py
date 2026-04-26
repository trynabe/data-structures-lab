class HashTable:
    def __init__(self, size):
        self.size = size
        # สร้างตารางแฮชที่เป็น list ว่างๆ ตามขนาด (จำลองลิงค์ลิสต์ในแต่ละช่อง)
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # ฟังก์ชันแฮช h(k) = k % 5 ตามที่ระบุในสไลด์
        return key % self.size

    def insert(self, key):
        # 1. หาตำแหน่ง index ก่อน
        index = self.hash_function(key)
        
        # 2. เพิ่มข้อมูลต่อท้ายเข้าไปใน list ของช่องนั้นๆ (จำลองการต่อสายโซ่)
        self.table[index].append(key)
        print(f"Calculated {key} % {self.size} = {index} -> Inserted {key} at index {index}")

    def display(self):
        print("\n--- Hash Table Structure ---")
        for i in range(self.size):
            # พิมพ์รูปแบบให้ดูเหมือนการชี้ลูกศรในลิงค์ลิสต์
            chain = " -> ".join(map(str, self.table[i]))
            print(f"Index {i}: [{chain}]")

# ขนาดตารางตามรูปคือ 5 (มี index 0 ถึง 4)
ht = HashTable(5)

# ข้อมูลที่ต้องการแทรกตามลำดับ: 7, 30, 19, 22, 25, 37
data = [7, 30, 19, 22, 25, 37]

print("--- Inserting Data ---")
for num in data:
    ht.insert(num)

ht.display()