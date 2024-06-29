from redis_om import HashModel
from .database import redis_db

class OrderModel(HashModel):
    product_id: str
    price: float
    tax: float
    total: float
    quantity: int
    status: str # pending, completed, refunded
    
    class Meta:
        database = redis_db