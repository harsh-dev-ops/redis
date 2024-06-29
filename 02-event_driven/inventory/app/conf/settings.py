from typing import Any, AnyStr
from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    REQUEST_TIME_OUT: int
    ORDER_SERVICE_URL: str
    ORDER_COMPLETED_QUEUE: str
    REFUND_ORDER_QUEUE: str
    PAYMENT_GROUP: str
    INVENTORY_GROUP:str
    
    
    BASE_PATH: AnyHttpUrl = Field(f"{Path(__file__).resolve().parent}", validate_default=False)
    
    class Config:
        env_file = '.env'
        
settings = Settings()