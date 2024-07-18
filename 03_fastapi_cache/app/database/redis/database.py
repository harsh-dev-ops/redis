import aioredis

async def get_redis() -> aioredis.Redis:
    redis_db = await aioredis.Redis(
        host='localhost',
        port=6378,
        db=1,
        encoding='utf-8',
        decode_responses=True
    )
    return redis_db