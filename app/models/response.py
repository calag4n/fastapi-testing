from typing import Generic
from typing import Optional
from typing import TypeVar

from pydantic.generics import GenericModel

ResultT = TypeVar('ResultT')


class Response(GenericModel, Generic[ResultT]):
    result: Optional[ResultT]
