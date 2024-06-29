from app.conf.settings import settings
from app.database import redis_db
import time

key=settings.REFUND_ORDER_QUEUE


async def refund_order(obj):
    redis_db.xadd(key, obj, "*")