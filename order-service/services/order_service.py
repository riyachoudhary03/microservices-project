from clients.user_client import get_user
from clients.product_client import get_product

orders = []

async def create_order(order_data):

    # 1. Validate user
    user = await get_user(order_data.user_id)

    # 2. Fetch product
    product = await get_product(order_data.product_id)

    # 3. Calculate price
    total_price = product["price"] * order_data.quantity

    # 4. Save order (temporary memory)
    order = {
        "user_id": user["id"],
        "product_name": product["name"],
        "quantity": order_data.quantity,
        "total_price": total_price
    }

    orders.append(order)

    return order