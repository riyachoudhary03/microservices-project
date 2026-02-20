
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app FIRST
app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Health Check ----------------
@app.get("/")
def home():
    return {"message": "API Gateway Running 🚀"}

# ---------------- ENV URLs ----------------
USER_SERVICE = os.getenv("USER_SERVICE_URL")
PRODUCT_SERVICE = os.getenv("PRODUCT_SERVICE_URL")
ORDER_SERVICE = os.getenv("ORDER_SERVICE_URL")

# ---------------- USERS ----------------
@app.get("/users")
async def get_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE}/users")
        return response.json()

# ---------------- PRODUCTS ----------------
@app.get("/products")
async def get_products():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PRODUCT_SERVICE}/products")
        return response.json()

# ---------------- ORDERS ----------------
@app.post("/orders")
async def create_order(request: Request):
    body = await request.json()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{ORDER_SERVICE}/orders",
            params=body
        )
        return response.json()