import os

from pydantic_settings import BaseSettings

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
env_file_path = os.path.join(parent_dir, ".env")
class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_BOT_NAME: str
    WEBAPP_PORT: str = "8080"
    WEBAPP_HOST: str = "localhost"

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

settings = Settings()