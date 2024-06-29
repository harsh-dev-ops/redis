from redis_om import HashModel
from .database import redis_db

class ProductModel(HashModel):
    name: str
    price: float
    quantity: int
    
    class Meta:
        database = redis_db