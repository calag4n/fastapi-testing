from typing import List

from api.controllers.connect import get_database
from api.controllers.users import add_user, get_users
from fastapi import APIRouter, status
from fastapi.params import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.User import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.post("/",
             response_model=User,
             response_description="User data added into the database",
             status_code=status.HTTP_201_CREATED)
async def create_user(user_in: User, db: AsyncIOMotorClient = Depends(get_database)):
    new_user = await add_user(user_in, db)
    return new_user


@router.get("/", response_model=List[User])
async def list_users(db: AsyncIOMotorClient = Depends(get_database)):
    users = await get_users(db)
    return users
