def multiply_by_indices(text):
    total = 0
    # ใช้ enumerate กำหนดให้ start=1 เพื่อให้ดัชนีเริ่มนับที่ 1 ตามสูตร
    for index, char in enumerate(text.upper(), start=1):
        # แปลงตัวอักษรเป็นตัวเลข (A=1, B=2, ..., Z=26)
        char_val = ord(char) - 64
        
        # นำค่าตัวอักษรมาคูณกับเลขดัชนีตำแหน่ง แล้วบวกสะสม
        total += (char_val * index)
        
    return total

# ทดสอบกับโจทย์ในสไลด์
word1 = "CAT"
word2 = "TAC"

print(f"f({word1}) = {multiply_by_indices(word1)}")
print(f"f({word2}) = {multiply_by_indices(word2)}")