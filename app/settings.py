from pydantic import BaseSettings


class MongoSettings(BaseSettings):
    HOST: str
    PORT: int
    DB: str

    class Config:
        env_prefix = 'MONGO_'
