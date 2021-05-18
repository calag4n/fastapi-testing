from uuid import UUID
from uuid import uuid4

from pydantic import Field
from pydantic import EmailStr

from .base import Base


class User(Base):
    uid: UUID = Field(default_factory=uuid4)
    email: EmailStr
    password: str
