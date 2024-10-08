import os
from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    EMAIL: str
    EMAIL_PASSWORD: str
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_USERNAME: str

    class Config:
        env_file = os.path.join(BASE_DIR, '.env')


settings = Settings()
