from redis_om import HashModel
from .database import redis_db

class Author(HashModel):
    name: str
    
    
    class Meta:
        database = redis_db
        
class Book(HashModel):
    name: str
    author: str
    price: float
    
    class Meta:
        database = redis_db