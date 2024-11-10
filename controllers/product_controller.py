# controllers/product_controller.py

from models.product_model import ProductModel

class ProductController:
    def __init__(self):
        self.product_model = ProductModel()

    def get_all_products(self):
        return self.product_model.get_all_products()

    def add_product(self, name, category, specification, unit, price, stock_quantity):
        self.product_model.add_product(name, category, specification, unit, price, stock_quantity)

    def update_product(self, product_id, **kwargs):
        self.product_model.update_product(product_id, **kwargs)

    def delete_product(self, product_id):
        self.product_model.delete_product(product_id)

    def close(self):
        self.product_model.close()
