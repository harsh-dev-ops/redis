import time

from app.models import OrderModel
from app.database import redis_db
from app.conf.settings import settings

async def order_complete(order: OrderModel):
    # time.sleep(0.1)
    order.status = 'completed'
    order.save()
    redis_db.xadd(settings.ORDER_COMPLETED_QUEUE, order.model_dump(), '*')