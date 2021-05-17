import uuid

from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        json_encoders = {
            uuid.UUID: str
        }
