from uuid import UUID
from typing import Optional

from pydantic import EmailStr

from .base import Base
from .fields import Fields


class UserUpdate(Base):
    uid: UUID = Fields.uid
    email: Optional[EmailStr] = Fields.email
    password: Optional[str] = Fields.password
