from aredis_om import HashModel, get_redis_connection
from app.conf.settings import settings

redis_db =  get_redis_connection(url=settings.REDIS_URL, decode_responses=True)

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