# app/crud/product.py
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductModel,ProductUpdate

def create_product(db: Session, product: ProductModel):
    db_product = Product(name=product.name, price=product.price, description=product.description)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db: Session):
    return db.query(Product).all()


def update_product(db:Session,product_id:int,product:ProductUpdate):
    
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    
    if product.name is not None:
        db_product.name = product.name
    if product.price is not None:
        db_product.price = product.price
    if product.description is not None:
        db_product.description = product.description

    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    
    db.delete(db_product)
    db.commit()
    return db_product