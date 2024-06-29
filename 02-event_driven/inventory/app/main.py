from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import inventory

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(
    inventory.router,
    tags=['Products'],
    prefix='/api/products',
)