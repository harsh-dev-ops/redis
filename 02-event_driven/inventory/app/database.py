import redis

redis_db = redis.Redis(
    host='localhost',
    port=6379,
    db=1,
    encoding='utf-8',
    decode_responses=True
)