from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str
    DB_PORT: int
    POOL_SIZE: int
    POOL_TIMEOUT: int
    POOL_RECYCLE: int
    MAX_OVERFLOW: int
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    LOG_DIR: str
    LOG_LEVEL: int

    class Config:
        env_file = ".env"


settings = Settings()
