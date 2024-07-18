from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from app.database.redis.database import redis_db

@asynccontextmanager
async def cache_lifespan(_: FastAPI) -> AsyncIterator[None]:
    FastAPICache.init(RedisBackend(redis_db), prefix="fastapi-cache")
    yield