import os

from typing import Any
from typing import Type
from typing import TypeVar

T = TypeVar('T', bound=Any)

sentinel: Any = object()


def getenv(type_: Type[T], key: str, default: T = sentinel) -> T:
    try:
        return type_(os.environ[key])

    except KeyError:
        if default is sentinel:
            raise

        return default
