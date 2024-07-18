import aioredis
from redis_om import HashModel

async def get_redis() -> aioredis.Redis:
    redis_db = await aioredis.Redis(
        host='localhost',
        port=6378,
        db=1,
        encoding='utf-8',
        decode_responses=True
    )
    return redis_db

redis_db = get_redis()

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