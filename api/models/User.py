from uuid import UUID, uuid4

from pydantic import EmailStr
from pydantic.main import BaseModel


class User(BaseModel):
    # id: UUID = uuid4()
    email: EmailStr
    password: str

    class Config:
        json_encoders = {UUID: str}
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "string"
            }
        }
