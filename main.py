from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
from database import get_db, engine
from schemas import Products, Users, Orders

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/product")
def get_product(db: Session = Depends(get_db)):
    all_products = db.query(models.Product).all()
    return all_products

@app.get("/user")
def get_user(db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()
    return all_users

@app.get("/order")
def get_order(db: Session = Depends(get_db)):
    all_orders = db.query(models.Order).all()
    return all_orders


@app.post("/product")
def create_product(product: Products, db: Session = Depends(get_db)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.post("/user")
def create_user(user: Users, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/order")
def create_order(order: Orders, db: Session = Depends(get_db)):
    new_order = models.Order(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@app.put("/product/update/{id}")
def update_product(id: int, product: Products, db: Session = Depends(get_db)):
    updated_product = db.query(models.Product).filter(models.Product.id == id).first()
    if updated_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} does not exist")

    updated_product.name = product.name
    updated_product.price = product.price
    updated_product.description = product.description

    db.commit()
    db.refresh(updated_product)

    return updated_product

@app.put("/user/update/{id}")
def update_user(id: int, user: Users, db: Session = Depends(get_db)):
    updated_user = db.query(models.User).filter(models.User.user_id == id).first()
    if updated_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")

    updated_user.lastname = user.lastname
    updated_user.firstname = user.firstname
    updated_user.middlename = user.middlename
    updated_user.address = user.address
    updated_user.phone = user.phone
    updated_user.email = user.email

    db.commit()
    db.refresh(updated_user)

    return updated_user

@app.put("/order/update/{id}")
def update_order(id: int, order: Orders, db: Session = Depends(get_db)):
    updated_order = db.query(models.Order).filter(models.Order.order_id == id).first()
    if updated_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {id} does not exist")

    updated_order.sale_date = order.sale_date
    updated_order.delivery_date = order.delivery_date
    updated_order.quantity = order.quantity

    db.commit()
    db.refresh(updated_order)

    return updated_order


@app.delete("/product/delete/{id}")
def delete_product(id: int, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT):
    delete_post = db.query(models.Product).filter(models.Product.id == id).first()

    if delete_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} does not exist")
    else:
        db.delete(delete_post)
        db.commit()

    return status_code

@app.delete("/user/delete/{id}")
def delete_user(id: int, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT):
    delete_post = db.query(models.User).filter(models.User.user_id == id).first()

    if delete_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
    else:
        db.delete(delete_post)
        db.commit()

    return status_code

@app.delete("/order/delete/{id}")
def delete_order(id: int, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT):
    delete_post = db.query(models.Order).filter(models.Order.order_id == id).first()

    if delete_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {id} does not exist")
    else:
        db.delete(delete_post)
        db.commit()

    return status_code