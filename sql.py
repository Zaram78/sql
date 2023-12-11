import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="boot",
    password="****"
)
mycursor = db.cursor()

mycursor.execute("CREATE DATABASE Shop")
mycursor.execute("USE Shop")

mycursor.execute("""
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255)
)
""")

mycursor.execute("""
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    category_id INT,
    price INT,
    quantity INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
)
""")

def add_product(product_name, category_id, price, quantity):
    mycursor.execute("INSERT INTO Products (product_name, category_id, price, quantity) VALUES (%s, %s, %s, %s)", (product_name, category_id, price, quantity))
    db.commit()

def add_category(category_name):
    mycursor.execute("INSERT INTO Categories (category_name) VALUES (%s)", (category_name,))
    db.commit()

def remove_product(product_id):
    mycursor.execute("DELETE FROM Products WHERE product_id = %s", (product_id,))
    db.commit()

def remove_category(category_id):
    mycursor.execute("DELETE FROM Categories WHERE category_id = %s", (category_id,))
    db.commit()

def edit_product(product_id, product_name, category_id, price, quantity):
    mycursor.execute("UPDATE Products SET product_name = %s, category_id = %s, price = %s, quantity = %s WHERE product_id = %s", (product_name, category_id, price, quantity, product_id))
    db.commit()

def edit_category(category_id, category_name):
    mycursor.execute("UPDATE Categories SET category_name = %s WHERE category_id = %s", (category_name, category_id))
    db.commit()

def search_products(name_or_category):
    mycursor.execute("SELECT * FROM Products WHERE product_name = %s OR category_id = (SELECT category_id FROM Categories WHERE category_name = %s)", (name_or_category, name_or_category))
    return mycursor.fetchall()

def search_categories(category_name):
    mycursor.execute("SELECT * FROM Categories WHERE category_name = %s", (category_name,))
    return mycursor.fetchall()

def display_products():
    mycursor.execute("SELECT * FROM Products")
    return mycursor.fetchall()

def display_categories():
    mycursor.execute("SELECT * FROM Categories")
    return mycursor.fetchall()
