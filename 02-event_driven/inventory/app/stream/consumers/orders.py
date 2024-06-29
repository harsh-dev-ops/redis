from pathlib import Path
import sys, time

BASE_PATH: str = Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(f"{BASE_PATH}")

from app.conf.settings import settings
from app.database import redis_db
from app.stream.producers.inventory import refund_order
from app.models import ProductModel

key = settings.ORDER_COMPLETED_QUEUE
group = settings.INVENTORY_GROUP


try:
    redis_db.xgroup_create(key, group)
except:
    print('Group already exists!')
    
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
                print(order_data)
                try:
                    product = ProductModel.get(order_data['product_id'])
                    
                    if product.quantity < int(order_data['quantity']):
                        raise Exception('Not enough quantity')
                    
                    product.quantity = product.quantity - int(order_data['quantity'])
                    product.save()
                    
                except Exception as e:
                    refund_order(order_data)
                    
    except Exception as e:
        print(f"{e}")
        
        
    