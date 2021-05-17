from typing import Generic
from typing import Union
from typing import Any
from typing import Optional
from typing import TypedDict
from typing import TypeVar

from pydantic import validator
from pydantic.generics import GenericModel

ResultT = TypeVar('ResultT')

__all__ = (
    'ResponseDict',
    'Response'
)


class ResponseResultDict(TypedDict):
    result: Any


class ResponseErrorDict(TypedDict):
    error: Optional[str]


ResponseDict = Union[ResponseResultDict, ResponseErrorDict]


class Response(GenericModel, Generic[ResultT]):
    result: Optional[ResultT]
    error: Optional[str]

    @validator('error', always=True)
    def check_consistency(
            cls, value: str, values: ResponseDict) -> str:
        result: Optional[ResultT] = values.get('result')  # type: ignore

        if value is None and result is None:
            raise ValueError(
                    'error and result cannot be None at the same time')

        if value is not None and result is not None:
            raise ValueError(
                    'error and result cannot be not None at the same time')

        return value
