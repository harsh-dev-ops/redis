from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REQUEST_TIME_OUT: int
    INVENTORY_SERVICE_URL: str
    ORDER_COMPLETED_QUEUE: str
    REFUND_ORDER_QUEUE: str
    PAYMENT_GROUP: str
    INVENTORY_GROUP: str
    
    class Config:
        env_file = '.env'
        
settings = Settings()