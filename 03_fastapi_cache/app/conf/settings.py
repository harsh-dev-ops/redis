from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    REDIS_URL:str = "redis://redis:6379"
    
    class Config:
        env_file = '.env'
        
settings = Settings()