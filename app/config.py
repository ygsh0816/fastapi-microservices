import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


def get_app_env():
    app_env = os.getenv('APP_ENV', 'dev')
    if app_env == 'prod':
        return '.env.prod'
    else:
        return '.env'


class Settings(BaseSettings):
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    SECRET_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file=get_app_env())


@lru_cache
def get_settings():
    return Settings()

