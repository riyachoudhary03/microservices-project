import httpx

PRODUCT_SERVICE_URL = "http://127.0.0.1:8002"

async def get_product(product_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")

        if response.status_code != 200:
            raise Exception("Product not found")

        return response.json()