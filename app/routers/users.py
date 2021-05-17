from uuid import UUID
from typing import List

from fastapi import APIRouter
from fastapi import FastAPI
from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse

from app.models import Response
from app.models import ResponseDict
from app.models import User
from app.models import UserCreate
from app.models import UserRead
from app.models import UserUpdate
from app.models import UserDelete
from app.controllers import users as users_controller

router = APIRouter(prefix='/users', tags=["users"])


class UsersException(Exception):
    def __init__(
        self,
        status_code: int,
        error_message: str = 'No message',
    ) -> None:
        self.status_code = status_code
        self.error_message = error_message


@router.post("/",
    response_model=Response[User],
    response_description='Create new user',
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(user_create: UserCreate) -> ResponseDict:
    try:
        result = await users_controller.create_user(user_create)

        if result is None:
            raise ValueError

        return {
            'result': result
        }

    except ValueError:
        return {
            'error': 'User has not created'
        }

@router.get("/",
    response_model=Response[List[User]],
    response_description='Get all users',
    response_model_exclude_none=True,
)
async def read_users() -> ResponseDict:
    try:
        result = await users_controller.read_users()

        if result is None:
            raise ValueError

        return {
            'result': result
        }

    except ValueError:
        return {
            'error': 'Internal error'
        }


@router.get("/{user_id}",
    response_model=Response[User],
    response_model_exclude_none=True,
)
async def read_user(user_id: UUID) -> ResponseDict:
    try:
        result = await users_controller.read_user(UserRead(id=user_id))

        if result is None:
            raise ValueError

        return {
            'result': result
        }

    except ValueError:
        return {
            'error': 'User has not been retrieved'
        }


@router.put("/",
    response_model=Response[User],
    response_description='Update user by id with email or/and password',
    response_model_exclude_none=True,
)
async def update_user(user_update: UserUpdate) -> ResponseDict:
    try:
        result = await users_controller.update_user(user_update)

        if result is None:
            raise ValueError

        return {
            'result': result
        }

    except ValueError:
        return {
            'error': 'User has not been updated'
        }



@router.delete("/{user_id}",
    response_model=Response[bool],
    response_description='Delete user by id',
    response_model_exclude_none=True,
)
async def delete_user(user_id: UUID) -> ResponseDict:
    try:
        result = await users_controller.delete_user(UserDelete(id=user_id))

        if result is None:
            raise ValueError

        return {
            'result': result
        }

    except ValueError:
        return {
            'error': 'User has not been updated'
        }


async def users_exception_handler(_: Request, exc: UsersException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'error': exc.error_message,
        },
    )


def setup(app: FastAPI) -> None:
    app.include_router(router)
    app.add_exception_handler(UsersException, users_exception_handler)
