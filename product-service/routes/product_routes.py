from fastapi import APIRouter, HTTPException
from typing import List
from models import Product
from services.product_service import (
    add_product,
    get_all_products,
    get_product_by_id
)

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Product service is alive"}


# Create Product
@router.post("/products", response_model=Product)
def create_product(product: Product):
    return add_product(product)


# Get All Products
@router.get("/products", response_model=List[Product])
def read_products():
    return get_all_products()


# Get Product by ID
@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int):
    product = get_product_by_id(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product