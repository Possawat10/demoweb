import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
DATABASE = 'coffee_shop.db'

# ฟังก์ชันเชื่อมต่อ database
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# ฟังก์ชันสร้าง database
def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db()
        cursor = conn.cursor()
        
        # สร้างตาราง categories
        cursor.execute('''
            CREATE TABLE categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')
        
        # สร้างตาราง coffee
        cursor.execute('''
            CREATE TABLE coffee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                image TEXT,
                stock INTEGER NOT NULL,
                category_id INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        ''')
        
        # เพิ่ม category ตัวอย่าง
        cursor.execute("INSERT INTO categories (name) VALUES ('Espresso')")
        cursor.execute("INSERT INTO categories (name) VALUES ('Latte')")
        cursor.execute("INSERT INTO categories (name) VALUES ('Cappuccino')")
        cursor.execute("INSERT INTO categories (name) VALUES ('Americano')")
        
        # เพิ่ม coffee ตัวอย่าง
        cursor.execute('''
            INSERT INTO coffee (name, price, image, stock, category_id)
            VALUES ('Classic Espresso', 50, 'espresso.jpg', 20, 1)
        ''')
        cursor.execute('''
            INSERT INTO coffee (name, price, image, stock, category_id)
            VALUES ('Iced Latte', 60, 'latte.jpg', 15, 2)
        ''')
        cursor.execute('''
            INSERT INTO coffee (name, price, image, stock, category_id)
            VALUES ('Hot Cappuccino', 65, 'cappuccino.jpg', 18, 3)
        ''')
        
        conn.commit()
        conn.close()
        print("✓ Database สร้างเรียบร้อยแล้ว")

# หน้าแรก - แสดงรายการกาแฟ
@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT coffee.id, coffee.name, coffee.price, coffee.image, 
               coffee.stock, categories.name as category
        FROM coffee
        JOIN categories ON coffee.category_id = categories.id
        ORDER BY coffee.id DESC
    ''')
    coffees = cursor.fetchall()
    conn.close()
    return render_template('index.html', coffees=coffees)

# หน้าเพิ่มสินค้า
@app.route('/add', methods=['GET', 'POST'])
def add():
    conn = get_db()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        image = request.form['image']
        stock = request.form['stock']
        category_id = request.form['category_id']
        
        cursor.execute('''
            INSERT INTO coffee (name, price, image, stock, category_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, price, image, stock, category_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    conn.close()
    return render_template('add.html', categories=categories)

# หน้าแก้ไขสินค้า
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        image = request.form['image']
        stock = request.form['stock']
        category_id = request.form['category_id']
        
        cursor.execute('''
            UPDATE coffee 
            SET name=?, price=?, image=?, stock=?, category_id=?
            WHERE id=?
        ''', (name, price, image, stock, category_id, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    cursor.execute('SELECT * FROM coffee WHERE id=?', (id,))
    coffee = cursor.fetchone()
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    conn.close()
    
    if coffee is None:
        return redirect(url_for('index'))
    
    return render_template('edit.html', coffee=coffee, categories=categories)

# ลบสินค้า
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM coffee WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
