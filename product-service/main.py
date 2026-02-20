from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()

# ✅ Allow frontend to access backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root route (testing server)
@app.get("/")
def home():
    return {"message": "Product Service is running"}

# ✅ Products API
@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Laptop", "price": 50000},
        {"id": 2, "name": "Phone", "price": 20000},
        {"id": 3, "name": "Headphones", "price": 3000},
    ]