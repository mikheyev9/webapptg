import os

from pydantic_settings import BaseSettings


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
env_file_path = os.path.join(parent_dir, ".env")
class Settings(BaseSettings):
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

settings = Settings()

DATABASE_URL = settings.DATABASE_URL
TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["_backend.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}