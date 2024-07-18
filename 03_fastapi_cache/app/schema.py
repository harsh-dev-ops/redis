from typing import Optional
from more_itertools import quantify
from pydantic import BaseModel, Field

class OrderIn(BaseModel):
    product_id: str
    quantity: int
    status: str = "pending"
    

class OrderUpdate(BaseModel):
    product_id: str | None = None  
    quantity: int | None = None 
    status: str | None = None
    
    
class OrderOut(OrderIn):
    pk: str
    price: float
    tax: float
    total: float
    
    class Config:
        orm_mode=True
    