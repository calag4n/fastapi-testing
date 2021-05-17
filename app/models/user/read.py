from uuid import UUID

from .base import Base
from .fields import Fields


class UserRead(Base):
    uid: UUID = Fields.uid
