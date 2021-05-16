from uuid import UUID, uuid4

from pydantic import EmailStr
from pydantic import Extra
from pydantic.main import BaseModel


class User(BaseModel):
    # id: UUID = uuid4()
    email: EmailStr
    password: str

    class Config:
        json_encoders = {UUID: str}
        extra = Extra.ignore
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "string"
            }
        }
