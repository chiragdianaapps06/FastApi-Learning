from pydantic import BaseModel
from typing import Optional

class ProductModel(BaseModel):
    name: str
    price: float
    # description: str
    description: Optional[str] = None  


class ProductModelWithoutDb(BaseModel):
    id: int
    name: str
    price: float

class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    description: str | None = None

class ProductOut(ProductModel):
    id: int