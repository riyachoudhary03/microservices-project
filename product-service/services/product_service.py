from models import Product

products = []

def add_product(product: Product):
    products.append(product)
    return product

def get_all_products():
    return products

def get_product_by_id(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return None