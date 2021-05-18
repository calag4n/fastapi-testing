from uuid import UUID
from typing import Any
from typing import TypedDict


class UserDictMixin(TypedDict):
    email: str
    password: str


class UserDictNative(UserDictMixin):
    uid: UUID


class UserDictTransmitted(UserDictMixin):
    uid: str


class ResponseDict(TypedDict):
    result: Any
