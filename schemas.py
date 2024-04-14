from pydantic import BaseModel
from typing import Optional
from datetime import date

class Products(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True
        tablename = "products"

class Users(BaseModel):
    user_id: Optional[int] = None
    lastname: Optional[str] = None
    firstname: Optional[str] = None
    middlename: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

    class Config:
        from_attributes = True
        tablename = "users"

class Orders(BaseModel):
    order_id: Optional[int] = None
    sale_date: Optional[date] = None
    delivery_date: Optional[date] = None
    quantity: Optional[int] = None
    user_id: Optional[int] = None
    product_id: Optional[int] = None

    class Config:
        from_attributes = True
        tablename = "orders"