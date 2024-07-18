import datetime
import time
from typing import Optional
import uvicorn

import redis.asyncio as async_redis

from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import Response

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from pydantic import EmailStr

from aredis_om.model import HashModel, NotFoundError
from aredis_om.connections import get_redis_connection

# This Redis instance is tuned for durability.
REDIS_DATA_URL = "redis://localhost:6378"

# This Redis instance is tuned for cache performance.
REDIS_CACHE_URL = "redis://localhost:6378"


class Customer(HashModel):
    first_name: str
    last_name: str
    email: EmailStr
    join_date: datetime.date
    age: int
    bio: Optional[str]

    # You can set the Redis OM URL using the REDIS_OM_URL environment
    # variable, or by manually creating the connection using your model's
    # Meta object.
    class Meta:
        database = get_redis_connection(url=REDIS_DATA_URL, decode_responses=True)


app = FastAPI()


@app.post("/customer")
async def save_customer(customer: Customer):
    # We can save the model to Redis by calling `save()`:
    return await customer.save()


@app.get("/customers")
async def list_customers(request: Request, response: Response):
    # To retrieve this customer with its primary key, we use `Customer.get()`:
    customers = await Customer.all_pks()
    result = [customer async for customer in customers]
    return {"customers": result}


@app.get("/customer/{pk}")
@cache(expire=10)
async def get_customer(pk: str, request: Request, response: Response):
    # To retrieve this customer with its primary key, we use `Customer.get()`:
    try:
        time.sleep(2)
        return await Customer.get(pk)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Customer not found")


@app.on_event("startup")
async def startup():
    r = async_redis.from_url(REDIS_CACHE_URL, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(r), prefix="fastapi-cache")

if __name__ == "__main__":
    uvicorn.run("cache:app", reload=True, host="0.0.0.0", port=8001)