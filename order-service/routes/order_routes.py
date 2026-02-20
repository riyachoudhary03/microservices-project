import os
from dotenv import load_dotenv

load_dotenv()

USER_SERVICE = os.getenv("USER_SERVICE_URL")
PRODUCT_SERVICE = os.getenv("PRODUCT_SERVICE_URL")

from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

# Service URLs (later come from ENV)
USER_SERVICE = "http://127.0.0.1:8001"
PRODUCT_SERVICE = "http://127.0.0.1:8002"


@router.post("/orders")
async def create_order(user_id: int, product_id: int):

    async with httpx.AsyncClient() as client:

        # ------------------------
        # Call USER SERVICE
        # ------------------------
        user_response = await client.get(f"{USER_SERVICE}/users")

        if user_response.status_code != 200:
            raise HTTPException(status_code=400, detail="User service error")

        users = user_response.json()

        user = next((u for u in users if u["id"] == user_id), None)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # ------------------------
        # Call PRODUCT SERVICE
        # ------------------------
        product_response = await client.get(f"{PRODUCT_SERVICE}/products")

        if product_response.status_code != 200:
            raise HTTPException(status_code=400, detail="Product service error")

        products = product_response.json()

        product = next((p for p in products if p["id"] == product_id), None)

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        # ------------------------
        # Create Order
        # ------------------------
        order = {
            "user": user,
            "product": product,
            "status": "Order Created"
        }

        return order