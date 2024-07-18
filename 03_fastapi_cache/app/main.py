from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import api_router

app = FastAPI(title="FastAPI Cache Example")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(
    api_router,
    prefix="/api",
)