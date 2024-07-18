from redis import asyncio as async_redis
from fastapi import Depends
from typing import Annotated

from app.conf.settings import settings

async def get_redis() -> async_redis.Redis:
    redis_db = await async_redis.from_url(settings.REDIS_URL, encoding="utf8", decode_responses=True)
    return redis_db

redis_db = Annotated[async_redis.Redis, Depends(get_redis)]