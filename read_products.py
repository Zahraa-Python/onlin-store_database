import sqlite3

connection = sqlite3.connect("market.db")
cursor = connection.cursor()

# أمر جلب (اختيار) كل البيانات من جدول المنتجات
cursor.execute("SELECT * FROM products")

# قراءة كل الصفوف التي وجدها الكود
all_products = cursor.fetchall()

print("--- المنتجات الموجودة في المتجر حالياً ---")
for product in all_products:
    print(product)

connection.close()