from redis_om import HashModel
from .database import redis_db

class AuthorModel(HashModel):
    name: str
    
    
    class Meta:
        database = redis_db
        
class BookModel(HashModel):
    name: str
    author: str
    price: float
    
    class Meta:
        database = redis_db