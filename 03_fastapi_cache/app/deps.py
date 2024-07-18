from fastapi import Depends
from typing import Annotated
from redis import Redis

from .database import redis_db

def get_db():
    try:
        yield redis_db
    except:

        print("Error occured")
        
db_dependency = Annotated[Redis, Depends(get_db)]
