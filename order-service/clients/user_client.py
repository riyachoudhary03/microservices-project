import httpx

USER_SERVICE_URL = "http://127.0.0.1:8001"

async def get_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/users/{user_id}")

        if response.status_code != 200:
            raise Exception("User not found")

        return response.json()