from uuid import uuid4

from pydantic import Field


class Fields:
    uid = Field(example=uuid4())
    email = Field(example='user@example.com')
    password = Field(example='secretStr0000')
