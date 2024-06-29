from typing import List
from fastapi import APIRouter, BackgroundTasks, HTTPException, Request, Response

from app.models import OrderModel
from app.schema import OrderIn, OrderOut, OrderUpdate
from .utils import inventory_request
from app.stream.producers.orders import order_complete

from ..deps import db_dependency

router = APIRouter()

@router.get('', response_model=List[OrderOut])
def get_orders(request: Request, response: Response, db: db_dependency, ):
    return [OrderModel.get(pk) for pk in OrderModel.all_pks()]
    

@router.get('/{pk}', response_model=OrderOut)
def get_order(request: Request, response: Response, pk: str):
    return OrderModel.get(pk)


@router.post('', response_model=OrderOut)
async def create_order(request: Request, 
                       response:Response, 
                       body:OrderIn, 
                       background_tasks: BackgroundTasks):
    order_data = body.model_dump()
    
    resp, status_code = await inventory_request(
        path=f"api/products/{order_data['product_id']}",
        method='get'
    )
    
    if order_data['quantity'] > resp['quantity']:
        raise HTTPException(
            status_code=400,
            detail="Inventory doesn't have enough products"
        )
        
    order_data['price'] = resp['price']
    order_data['tax'] = resp['price'] * 0.18
    order_data['total'] = (order_data['price'] + order_data['tax']) * order_data['quantity']
    
    order = OrderModel(**order_data)
    order.save()
    
    background_tasks.add_task(order_complete, order)
    
    return order


@router.patch('/{pk}', response_model = OrderOut)
def update_Order(request: Request, response: Response, pk: str, body: OrderUpdate):
    data = body.model_dump(exclude_defaults=True)
    
    order = OrderModel.get(pk)
    
    for col, value in data.items():
        setattr(order, col, value)
        
    order.save()
    return order


@router.delete('/{pk}')
def delete_order(request: Request, response: Response, pk: str):
    return OrderModel.delete(pk)
    