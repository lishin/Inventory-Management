# models/sales_model.py

from .database import get_connection

class SalesModel:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def get_sales_data_by_date(self):
        self.cursor.execute('''
            SELECT date(sale_date) as sale_day, SUM(quantity) as total_sales
            FROM sales
            GROUP BY sale_day
            ORDER BY sale_day
        ''')
        return self.cursor.fetchall()

    def add_sale(self, product_id, quantity):
        self.cursor.execute('''
            INSERT INTO sales (product_id, quantity)
            VALUES (?, ?)
        ''', (product_id, quantity))
        self.conn.commit()

    def close(self):
        self.conn.close()
