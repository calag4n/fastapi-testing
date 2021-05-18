from uuid import UUID
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from fastapi import APIRouter
from fastapi import FastAPI
from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import EmailStr

from api.models import Response
from api.models import User
from api.models import UserCreate
from api.models import UserRead
from api.models import UserUpdate
from api.models import UserDelete
from api.controllers import users as users_controller

if TYPE_CHECKING:
    from api.hints import UserDictNative
    from api.hints import ResponseDict

router = APIRouter(prefix='/users', tags=["users"])


class UsersException(Exception):
    def __init__(
        self,
        status_code: int,
        error_message: str = 'No message',
    ) -> None:
        self.status_code = status_code
        self.error_message = error_message


@router.post(
    "/",
    response_model=Response[User],
    response_description='Create new user',
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(user_create: UserCreate) -> 'ResponseDict':
    created_user: 'UserDictNative' = await users_controller.create_user(
        user_create)

    if created_user is None:
        raise UsersException(400, 'User has not created')

    return {'result': created_user}


@router.get(
    "/",
    response_model=Response[List[User]],
    response_description='Get all users',
    response_model_exclude_none=True,
)
async def read_users() -> 'ResponseDict':
    try:
        result = await users_controller.read_users()

        return {'result': result}

    except Exception as e:
        raise UsersException(500, f'{type(e).__name__}({e})')


@router.get(
    "/{user_uid}",
    response_model=Response[User],
    response_description=(
        'Retrieve specic user by user uid not mongo _id, but uuid)'),
    response_model_exclude_none=True,
)
async def read_user(user_uid: UUID) -> 'ResponseDict':
    retrieved_user: 'UserDictNative' = await users_controller.read_user(
        user_uid=user_uid)

    if retrieved_user is None:
        raise UsersException(400, 'User has not been retrieved')

    return {'result': retrieved_user}


@router.put(
    "/{user_uid}",
    response_model=Response[User],
    response_description=(
        'Update specic user by user id not mongo _id, but uuid) '
        'with email and/or password'),
    response_model_exclude_none=True,
)
async def update_user(user_uid: UUID,
                      user_update: UserUpdate) -> 'ResponseDict':
    updated_user: 'UserDictNative' = await users_controller.update_user(
        user_uid=user_uid,
        user_update=user_update,
    )

    if updated_user is None:
        raise UsersException(400, 'User has not been updated')

    return {'result': updated_user}


@router.delete(
    "/{user_uid}",
    response_model=Response[bool],
    response_description='Delete user by uid',
    response_model_exclude_none=True,
)
async def delete_user(user_uid: UUID) -> 'ResponseDict':
    is_deleted: bool = await users_controller.delete_user(user_uid=user_uid)

    if not is_deleted:
        raise UsersException(400, 'User has not been deleted')

    return {
        'result': is_deleted  # It's always true. Maybe it's needed to change
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
