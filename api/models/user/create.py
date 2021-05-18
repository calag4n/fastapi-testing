from pydantic import EmailStr

from .base import Base
from .fields import Fields


class UserCreate(Base):
    email: EmailStr = Fields.email
    password: str = Fields.password
