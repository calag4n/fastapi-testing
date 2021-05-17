from typing import Generic
from typing import Any
from typing import Optional
from typing import TypedDict
from typing import TypeVar

from pydantic.generics import GenericModel

ResultT = TypeVar('ResultT')

__all__ = (
    'ResponseDict',
    'Response'
)


class ResponseDict(TypedDict):
    result: Any


class Response(GenericModel, Generic[ResultT]):
    result: Optional[ResultT]
