from typing import Optional
from more_itertools import quantify
from pydantic import BaseModel, Field

class ProductIn(BaseModel):
    name: str
    quantity: int
    price: float
    

class ProductUpdate(BaseModel):
    name: str | None = None
    quantity: int | None = None
    price: float | None =  None
    
    
class ProductOut(ProductIn):
    pk: str
    
    class Config:
        orm_mode=True
    