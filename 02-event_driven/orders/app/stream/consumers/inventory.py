from pathlib import Path
import sys, time
BASE_PATH: str = Path(__file__).resolve().parent.parent.parent.parent

sys.path.append(f"{BASE_PATH}")

from app.conf.settings import settings
from app.database import redis_db
from app.stream.producers.orders import order_complete
from app.models import OrderModel

try:
    key = settings.REFUND_ORDER_QUEUE
    group = settings.PAYMENT_GROUP
    redis_db.xgroup_create(key, group)
except Exception as e:
    print(f"{e}")
    print("Group already created!")
    

def decode_result(result):
    key = result[0]
    pk = result[1][0][0]
    data = result[1][0][1]
    return {'data': data, 'pk': pk, 'key': key}
    
while True:
    try:
        results = redis_db.xreadgroup(group, key, {key: '>'}, None)
        
        if results != []:
            for result in results:
                order_data = decode_result(result)['data']
                order = OrderModel.get(order_data['pk'])
                order.status = 'refunded'
                order.save()
            
    except Exception as e:
        print(f"{e}")
    time.sleep(1)