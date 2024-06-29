from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import orders

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(
    orders.router,
    tags=['Orders'],
    prefix='/api/Orders',
)