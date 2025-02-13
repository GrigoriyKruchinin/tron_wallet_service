from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Tron wallet service"
    DATABASE_URL: str
    postgres_user: str
    postgres_password: str
    postgres_db: str

    tron_network: str = "mainnet"

    model_config = SettingsConfigDict(env_file=".env")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if "TEST_ENV" in kwargs and kwargs["TEST_ENV"] == "True":
            self.DATABASE_URL = "postgresql://test_user:test_password@localhost/test_db"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
