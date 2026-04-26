def mid_square_hash(key, r):
    # 1. นำค่ากุญแจแฮชมายกกำลังสอง
    squared = key ** 2
    squared_str = str(squared)
    
    length = len(squared_str)
    
    # ดักไว้เผื่อกรณีที่ผลลัพธ์การยกกำลังสองมีจำนวนหลักน้อยกว่า r ให้เติม 0 ข้างหน้า
    if length < r:
        squared_str = squared_str.zfill(r)
        length = len(squared_str)
        
    # 2. คำนวณหา index เริ่มต้นเพื่อตัดตัวเลขตรงกลาง
    start_index = (length - r) // 2
    end_index = start_index + r
    
    # ตัดเอาเฉพาะเลขตรงกลางจำนวน r ตัว
    middle_digits = squared_str[start_index:end_index]
    
    return int(middle_digits), squared_str

# --- ทดสอบตามตัวอย่างแรกในสไลด์ ---
k1 = 60
r1 = 2
result1, sq1 = mid_square_hash(k1, r1)
print("--- Example 1 ---")
print(f"Key (k) = {k1}")
print(f"Squared (k^2) = {sq1}")
print(f"Hash Value h(k) = {result1}\n")

# --- ทดสอบโจทย์ด้านล่างของสไลด์ ---
k2 = 87654
r2 = 2
result2, sq2 = mid_square_hash(k2, r2)
print("--- Exercise ---")
print(f"Key (k) = {k2}")
print(f"Squared (k^2) = {sq2}")
print(f"Hash Value h(k) = {result2}")