from fastapi import APIRouter, Depends

from app.database.redis.database import redis_db


router  = APIRouter()

