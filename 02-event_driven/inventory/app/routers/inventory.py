from typing import List
from fastapi import APIRouter, Request, Response

from app.models import ProductModel
from app.schema import ProductIn, ProductOut, ProductUpdate

from ..deps import db_dependency

router = APIRouter()

@router.get('', response_model=List[ProductOut])
def get_products(request: Request, response: Response, db: db_dependency, ):
    return [ProductModel.get(pk) for pk in ProductModel.all_pks()]
    

@router.get('/{pk}', response_model=ProductOut)
def get_product(request: Request, response: Response, pk: str):
    return ProductModel.get(pk)


@router.post('', response_model=ProductOut)
def create_product(request: Request, response:Response, body:ProductIn):
    data = body.model_dump()
    product = ProductModel(**data)
    return product.save()


@router.patch('/{pk}', response_model = ProductOut)
def update_product(request: Request, response: Response, pk: str, body: ProductUpdate):
    data = body.model_dump(exclude_defaults=True)
    
    product = ProductModel.get(pk)
    
    for col, value in data.items():
        setattr(product, col, value)
        
    product.save()
    return product


@router.delete('/{pk}')
def delete_product(request: Request, response: Response, pk: str):
    return ProductModel.delete(pk)
    