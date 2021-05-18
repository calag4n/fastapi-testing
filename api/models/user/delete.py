from uuid import UUID

from .base import Base
from .fields import Fields


class UserDelete(Base):
    uid: UUID = Fields.uid

