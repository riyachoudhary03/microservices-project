from pydantic import BaseModel

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class OrderResponse(BaseModel):
    user_id: int
    product_name: str
    quantity: int
    total_price: float