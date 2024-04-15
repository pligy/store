from sqlalchemy import String, Integer, Column, Numeric, ForeignKey, Date
from sqlalchemy.orm import relationship

from database.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    description = Column(String)
    order = relationship("Order", back_populates="products")

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    lastname = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    middlename = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    order = relationship("Order", back_populates="users")

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, nullable=False)
    sale_date = Column(Date, nullable=False)
    delivery_date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    users = relationship("User", back_populates="order")
    product_id = Column(Integer, ForeignKey("products.id"))
    products = relationship("Product", back_populates="order")
