from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.order_routes import router as order_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Order Service Running"}

app.include_router(order_router)