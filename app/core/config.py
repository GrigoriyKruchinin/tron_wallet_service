from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Tron wallet service"
    DATABASE_URL: str
    postgres_user: str
    postgres_password: str
    postgres_db: str

    api_tron_key: str
    tron_network: str = "mainnet"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
