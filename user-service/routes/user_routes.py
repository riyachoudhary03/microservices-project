from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# ------------------
# User Model
# ------------------
class User(BaseModel):
    id: int
    name: str
    email: str

users_db = []

# ------------------
# Routes
# ------------------

@router.get("/users")
def get_users():
    return users_db


@router.post("/users")
def create_user(user: User):
    users_db.append(user)
    return {"message": "User created", "user": user}