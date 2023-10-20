from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path='../.env', verbose=True)

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    
settings = Settings()
