from fastapi import APIRouter

from app.database.redis.database import redis_db
from . import authors


api_router = APIRouter()

@api_router.get('/redis/connection', tags=["Redis"])
async def db_check(redis_db:redis_db):
    return redis_db.connection_pool.connection_kwargs

api_router.include_router(
    authors.router, 
    prefix="/authors", 
    tags=["Authors"]
    )