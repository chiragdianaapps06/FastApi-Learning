from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db
from app.schemas.product import ProductModel,ProductUpdate,ProductOut
from app.crud.product import create_product ,get_product,get_products,update_product,delete_product
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/", response_model = ProductOut)
def create_product_api(product:ProductModel, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

@router.get("/{product_id}/", response_class= JSONResponse)
def get_product_api(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db=db, product_id=int(product_id))
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message":"Fetch data successfully.","data":db_product}

@router.get("/",response_class= JSONResponse)
def list_products_api( db: Session = Depends(get_db)):
    products = get_products(db=db)
    return {"message":"Fetch data successfully.","data":products}
# skip: int = 0, limit: int = 100,, skip=skip, limit=limit


@router.put("/{product_id}/",response_model= ProductOut)
def update_product_api(product_id:int,product:ProductUpdate,db:Session = Depends(get_db)):
    db_product = update_product(db,product_id,product)
    
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return db_product



@router.delete("/{product_id}", response_model=schemas.product.ProductOut)
def delete_product_api(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_product(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product