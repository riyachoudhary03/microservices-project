import requests
from models import User

# temporary database
users = []

def add_user(user: User):
    users.append(user)
    return user

def get_all_users():
    return users

def get_products_from_product_service():
    response = requests.get("http://127.0.0.1:8002/products")
    return response.json()

def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
