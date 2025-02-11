from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    local_directory: str
    redis_url:str
    model_config = SettingsConfigDict(env_file=".env")

settings= Settings()