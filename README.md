# ☕ Coffee Shop Web Application

เว็บแอปพลิเคชันร้านกาแฟ สร้างด้วย Flask และ SQLite ที่เหมาะสำหรับนักศึกษาปี 1

## 📋 ฟีเจอร์

✅ **แสดงรายการกาแฟ** - หน้าแรกแสดงกาแฟทั้งหมด พร้อม category
✅ **เพิ่มสินค้า** - เพิ่มกาแฟใหม่ได้ง่ายๆ
✅ **แก้ไขสินค้า** - แก้ไขข้อมูลกาแฟที่มีอยู่
✅ **ลบสินค้า** - ลบกาแฟออกจากรายการ
✅ **ระบบ Category** - จัดกาแฟตามหมวดหมู่
✅ **ตัวอย่างข้อมูล** - มีข้อมูลตัวอย่างให้ใช้ทดสอบ

## 📁 โครงสร้างไฟล์

```
Demoweb/
├── app.py                 # ไฟล์หลักของแอปพลิเคชัน
├── coffee_shop.db         # ฐานข้อมูล (สร้างอัตโนมัติ)
├── requirements.txt       # Dependencies
└── templates/
    ├── index.html        # หน้าแรก - แสดงรายการกาแฟ
    ├── add.html          # หน้าเพิ่มสินค้า
    └── edit.html         # หน้าแก้ไขสินค้า
```

## 🗄️ ฐานข้อมูล

### ตาราง `categories`
```
id (INTEGER) - Primary Key
name (TEXT) - ชื่อหมวดหมู่
```

### ตาราง `coffee`
```
id (INTEGER) - Primary Key
name (TEXT) - ชื่อกาแฟ
price (REAL) - ราคา
image (TEXT) - ลิงค์รูปภาพ
stock (INTEGER) - จำนวนสต๊อก
category_id (INTEGER) - Foreign Key (categories.id)
```

## 🚀 วิธีการใช้

### 1. ติดตั้ง Python Packages
```bash
pip install -r requirements.txt
```

### 2. รันแอปพลิเคชัน
```bash
python app.py
```

### 3. เข้าใช้งาน
- เปิดเบราว์เซอร์ไปที่ `http://localhost:5000`
- คลิก "เพิ่มสินค้าใหม่" เพื่อเพิ่มกาแฟ
- คลิก "แก้ไข" เพื่อแก้ไขข้อมูล
- คลิก "ลบ" เพื่อลบสินค้า

## 💡 รายละเอียดโค้ด

### app.py - ส่วนสำคัญ

**`get_db()`** - เชื่อมต่อฐานข้อมูล
```python
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
```

**`init_db()`** - สร้างตารางและข้อมูลตัวอย่าง
```python
def init_db():
    # สร้างตาราง categories
    # สร้างตาราง coffee
    # เพิ่มข้อมูลตัวอย่าง
```

**Routes (เส้นทาง)**
- `/` - แสดงรายการกาแฟ
- `/add` - เพิ่มสินค้า
- `/edit/<id>` - แก้ไขสินค้า
- `/delete/<id>` - ลบสินค้า

## 🎨 Frontend

**ใช้ Jinja2 Template** - แสดงข้อมูลจาก Python ใน HTML

```html
<!-- ตัวอย่าง: Loop แสดงกาแฟทั้งหมด -->
{% for coffee in coffees %}
    <div class="coffee-card">
        <h3>{{ coffee['name'] }}</h3>
        <p>฿{{ coffee['price'] }}</p>
    </div>
{% endfor %}
```

## 📝 ตัวอย่างการใช้

### เพิ่มกาแฟ
1. คลิก "เพิ่มสินค้าใหม่"
2. กรอกชื่อ: "Iced Americano"
3. กรอกราคา: "55"
4. กรอกสต๊อก: "25"
5. เลือก Category: "Americano"
6. คลิก "บันทึก"

### แก้ไขกาแฟ
1. คลิก "แก้ไข" ที่สินค้าที่ต้องการ
2. แก้ไขข้อมูล
3. คลิก "บันทึกการเปลี่ยนแปลง"

### ลบกาแฟ
1. คลิก "ลบ"
2. ยืนยันการลบ

## 🛠️ เทคโนโลยีที่ใช้

| ส่วนประกอบ | เทคโนโลยี |
|-----------|----------|
| Backend | Flask |
| Database | SQLite 3 |
| Frontend | HTML5, CSS3, Jinja2 |
| Python | 3.8+ |

## 📚 หลักการเรียนรู้

- **MVC Pattern** - Model (Database), View (HTML), Controller (Flask routes)
- **SQL Basics** - SELECT, INSERT, UPDATE, DELETE
- **Foreign Keys** - ความสัมพันธ์ระหว่างตาราง
- **Flask Routing** - สร้างเส้นทาง URL
- **Template Rendering** - แสดงข้อมูลใน HTML

## ⚠️ หมายเหตุสำหรับนักศึกษา

1. **ฐานข้อมูล** - ถูกสร้างอัตโนมัติเมื่อรันแอปครั้งแรก
2. **ข้อมูลตัวอย่าง** - เพิ่มอัตโนมัติเพื่อทดสอบ
3. **รูปภาพ** - ใช้ URL ที่อยู่บนอินเทอร์เน็ต หรือโฟลเดอร์ `static/`
4. **ยังไม่มี Authentication** - ทุกคนสามารถเพิ่ม/แก้ไข/ลบได้

## 🔄 ขั้นตอนการทำงาน

```
User เข้าเว็บ
    ↓
Flask ดึงข้อมูลจาก SQLite
    ↓
render_template() แสดง HTML
    ↓
User กรอกฟอร์มและ submit
    ↓
Flask ประมวลผลและเขียนลง Database
    ↓
Redirect ไปหน้าแรก
```

## 📞 ติดต่อ / ปัญหา

ถ้ามีปัญหา:
1. ตรวจสอบว่า Python 3.8+ ได้ติดตั้ง
2. ติดตั้ง requirements: `pip install -r requirements.txt`
3. ตรวจสอบท่าสั้ๆ ที่พอร์ต 5000 ว่างอยู่

---

**สร้างด้วย ❤️ สำหรับนักศึกษา**
