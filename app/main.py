# from typing import Union
# from pydantic import BaseModel, EmailStr
# from fastapi import FastAPI,Request,Depends,HTTPException


# from fastapi.responses import JSONResponse,PlainTextResponse

# from database import engine, SessionLocal, Base
# import models.product
# from sqlalchemy.orm import Session
# # Base.metadata.create_all(bind=engine)
# app = FastAPI()

# # Dependency for DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# class user_data(BaseModel):
#     name : str
#     email : EmailStr
#     phone : int


# # def auth_user(request:Request):
# #     if request.get("auth"):
# #         return True
# #     else:
# #         raise HTTPException('unauthrised')

# @app.get("/test")
# def read_root():
#     return {"Hello": "World"}


# # @app.get("/items/{item_id}")
# # def read_item(item_id: int, q: Union[str, None] = None):
# #     return {"item_id": item_id, "q": q}

# # @app.post('/test')
# # def get_test(data :user_data,request:Request,user:dict=Depends(auth_user)):
# #     print(request.headers)
# #     return "hello"

# # product = []
# # @app.post("/product")
# # def create_product(name:str):
# #     product.append(name)
# #     return f"product created succussfully {name} -- {len(product)}"


# # @app.get("/list-product")
# # def list_product():
# #     # product.append(name)
# #     return product

# # @app.post('/greeting',response_class=JSONResponse)
# # def greeting(user:user_data,name:str):
# #     print(f"Your name is {name}.")
    
# #     return {
# #         "name":user.name,
# #         "email":user.email,
# #         "phone":user.phone
# #         }



# # @app.post('/greeting1',response_class=PlainTextResponse)
# # def greeting1(user:user_data,name:str):
# #     print(f"Your name is {name}.")
    
# #     return f"{user.name},{user.email},{user.phone}"

# class ProductModelWithoutDb(BaseModel):
#     id : int
#     name : str
#     price : float


# class ProductModel(BaseModel):
#     # id : int
#     name : str
#     price : float
#     description:str


# products = {}

# # @app.post('/product',response_class=JSONResponse)
# # def product(data:product_model):
# #     product.add(id = data.id,name = data.name,price = data.price)
# #     return {
# #         "id":data.id,
# #         "name":data.name,
# #         "price":data.price
# #     }
# @app.post("/product/", response_class=JSONResponse)
# def create_product(data: ProductModelWithoutDb):
#     if data.id in products:
#         return JSONResponse(content={"error": "Product ID already exists"}, status_code=400)
    
#     products[data.id] = {"name": data.name, "price": data.price}
#     return {"message": "Product created successfully", "data": {"id":data.id, "name":data.name,"price":data.price}}


# @app.get('/product/')
# def list_product():

#     return {"products":products}

# print(products)

# # @app.get('/product/{id}/')
# # def get_product(id:int):

# #     product = products[id]
# #     # return {"message":"fetch product successfully","data":{"id":id,"name":product.name,"price":product.price}}
# #     return {"message":"fetch product successfully","data":product.dict()}


# @app.get("/product/{id}/")
# def get_product(id: int):
#     product = products.get(id)
#     if not product:
#         return {"message": "Product not found"}
#     return {"message": "fetch product successfully",
#             "data": {"id": id, "name": product["name"], "price": product["price"]}}

# @app.put("/product/{id}/")
# def update_product(id: int, data: ProductModelWithoutDb):
#     product = products.get(id)
#     if not product:
#         return {"message": "Product not found"}

#     if data.name:
#         product["name"] = data.name
#     if data.price:
#         product["price"] = data.price

#     return {
#         "message": "product updated successfully",
#         "data": {"id": id, "name": product["name"], "price": product["price"]}
#     }

# @app.delete("/product/{id}/")
# def delete_product(id: int):
   
#     product = products.get(id)
#     products.pop(id)
#     return {
#         "message": "product deleted successfully",
#         "data": {"id": id, "name": product["name"], "price": product["price"]}
#     }



# @app.post("/products/")
# def create_product(product: ProductModel, db: Session = Depends(get_db)):
#     db_product = models.Product(name=product.name, price=product.price)
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product

# @app.get("/products/{product_id}")
# def get_product(product_id: int, db: Session = Depends(get_db)):
#     product = db.query(models.Product).filter(models.Product.id == product_id).first()
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return product


# @app.get("/products/")
# def list_products(db: Session = Depends(get_db)):
#     return db.query(models.Product).all()


# app/main.py
from fastapi import FastAPI
from app.api import product,user

app = FastAPI()

app.include_router(product.router, prefix="/products", tags=["Products"])

app.include_router(user.router,prefix='/users')
