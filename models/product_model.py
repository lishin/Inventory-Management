# models/product_model.py

from .database import get_connection

class ProductModel:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def get_all_products(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def add_product(self, name, category, specification, unit, price, stock_quantity):
        self.cursor.execute('''
            INSERT INTO products (name, category, specification, unit, price, stock_quantity)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, category, specification, unit, price, stock_quantity))
        self.conn.commit()

    def update_product(self, product_id, **kwargs):
        fields = ', '.join(f"{k} = ?" for k in kwargs.keys())
        values = list(kwargs.values()) + [product_id]
        self.cursor.execute(f'''
            UPDATE products SET {fields} WHERE product_id = ?
        ''', values)
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('DELETE FROM products WHERE product_id = ?', (product_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
