<div align="center">

# 🌐 Graph Algorithms
### *Detailed Study Notes*

📚 **Dijkstra's Algorithm**  
📚 **Prim-Jarnik Algorithm**  
📚 **Kruskal's Algorithm**

---

</div>

# ① Dijkstra's Algorithm

> ## 🎯 ปัญหาที่แก้
ใช้สำหรับหาเส้นทางที่สั้นที่สุดจากจุดเริ่มต้นเพียงจุดเดียวไปยังจุดอื่น ๆ ทั้งหมดในกราฟ  
(**Single-Source Shortest Paths**)

---

## ⚠️ เงื่อนไขการใช้งาน

✔️ ใช้ได้กับ **Weighted Graph**  
✔️ ค่าน้ำหนักต้องเป็น **Non-negative weights**

❌ ใช้ไม่ได้ถ้ามีน้ำหนักติดลบ

---

## 💡 แนวคิดหลัก

จัดเป็น **Greedy Algorithm** ชนิดหนึ่ง

มีพื้นฐานแนวคิดต่อยอดจากการแวะผ่านกราฟแนวกว้าง  
(**Breadth-First Traversal**)

ใช้งานร่วมกับ

- **Priority Queue**
- การเก็บระยะทางปัจจุบัน
- การเลือกเวอร์เท็กซ์ที่ดีที่สุดในแต่ละรอบ

---

## ⚙️ วิธีการทำงาน

### Step 1 — Initialize

กำหนดค่าเริ่มต้น

$$
D[s] = 0
$$

และสำหรับทุกเวอร์เท็กซ์อื่น

$$
D[v] = \infty
$$

---

### Step 2 — Insert

นำทุกเวอร์เท็กซ์ใส่ใน **Priority Queue**

---

### Step 3 — Extract Minimum

ดึงเวอร์เท็กซ์ $u$ ที่มีระยะทางน้อยที่สุดออกจาก Queue

---

### Step 4 — Relaxation

ตรวจสอบเวอร์เท็กซ์ $v$ ที่ประชิดกับ $u$

หาก

$$
D[u] + w(u,v) < D[v]
$$

ให้ปรับค่า

$$
D[v]
$$

ใหม่ และอัปเดต Queue

---

### Step 5 — Repeat

ทำซ้ำจน Queue ว่างเปล่า

---

## ⏱️ Time Complexity

| Structure | Complexity |
|----------|------------|
| Heap | $O((n+m)\log n)$ |
| Unsorted Sequence | $O(n^2)$ |

โดยที่

- $n$ = จำนวนเวอร์เท็กซ์
- $m$ = จำนวนเอดจ์

---

---

# ② Prim-Jarnik Algorithm

> ## 🎯 ปัญหาที่แก้
ใช้สำหรับหา **Minimum Spanning Tree (MST)**

ต้นไม้ที่เชื่อมต่อทุกจุดในกราฟเข้าด้วยกัน  
โดยมีผลรวมค่าน้ำหนักน้อยที่สุด

---

## 💡 แนวคิดหลัก

เป็น **Greedy Algorithm**

เริ่มต้นจากเวอร์เท็กซ์ใดเวอร์เท็กซ์หนึ่ง  
แล้วค่อย ๆ ขยาย MST

หลักสำคัญคือ

> เลือกเอดจ์ที่มีค่าน้ำหนักน้อยที่สุด  
> ที่เชื่อมกับเวอร์เท็กซ์ใหม่เสมอ

---

## ⚙️ วิธีการทำงาน

### Step 1 — Initialize

กำหนดค่าเริ่มต้น

$$
D[s] = 0
$$

และจุดอื่นเป็น

$$
\infty
$$

---

### Step 2 — Extract

ดึงเวอร์เท็กซ์ $u$  
ที่มีค่าคีย์น้อยที่สุดออกจาก Priority Queue

และเชื่อมเข้ากับ MST

---

### Step 3 — Update Neighbor

ตรวจสอบเวอร์เท็กซ์ $v$

หาก

$$
w(u,v) < D[v]
$$

ให้ปรับค่า

$$
D[v]
$$

ใหม่เป็นน้ำหนักของเอดจ์นั้น

แล้วอัปเดต Queue

---

## ⏱️ Time Complexity

$$
O(m \log n)
$$

สำหรับ Connected Graph  
เมื่อใช้ Heap

---

---

# ③ Kruskal's Algorithm

> ## 🎯 ปัญหาที่แก้
หา **Minimum Spanning Tree (MST)**  
เช่นเดียวกับ Prim-Jarnik Algorithm

---

## 💡 แนวคิดหลัก

เป็น **Greedy Algorithm**

แตกต่างจาก Prim ตรงที่

❌ ไม่เริ่มจากเวอร์เท็กซ์

แต่จะ

✅ พิจารณาเอดจ์ที่มีน้ำหนักน้อยที่สุดก่อน

---

## 🌲 มุมมองแบบ Cluster

ตอนเริ่มต้น

แต่ละเวอร์เท็กซ์คือ **1 Cluster**

ตัวอย่าง

```text
A   B   C   D