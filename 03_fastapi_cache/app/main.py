from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from app.routers import api_router
from app.database.redis.database import redis_db
from app.cache.lifespan import cache_lifespan

app = FastAPI(title="FastAPI Cache Example", lifespan=cache_lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(
    api_router,
    prefix="/api",
)

# @app.on_event("startup")
# async def startup():
#     FastAPICache.init(RedisBackend(redis_db), prefix="fastapi-cache")