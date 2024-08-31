from datetime import datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from tortoise.exceptions import IntegrityError

from _backend.models import User
from _backend.utils.birthday_calculator import calculate_time_until_birthday
from _backend.logging_config import logger

router = APIRouter()

class UserCreate(BaseModel):
    first_name: str = ""
    last_name: str = ""
    username: str
    birth_date: str


class UserResponse(BaseModel):
    first_name: str
    last_name: str
    username: str
    time_until_birthday: dict


@router.post("/users/", response_model=UserResponse)
async def create_or_update_user(user: UserCreate):
    logger.info(f"Received user data: {user}")

    birth_date_obj = datetime.fromisoformat(user.birth_date.replace("Z", "+00:00")).date()
    existing_user = await User.get_or_none(username=user.username)

    if existing_user:
        existing_user.first_name = user.first_name
        existing_user.last_name = user.last_name
        existing_user.birth_date = birth_date_obj
        await existing_user.save()
        user_obj = existing_user
        logger.info(f"Updated user: {user.username}")
    else:
        try:
            user_obj = await User.create(
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                birth_date=birth_date_obj,
            )
            logger.info(f"Created new user: {user.username}")
        except IntegrityError as e:
            logger.error(f"Error creating user: {str(e)}")
            raise HTTPException(status_code=400, detail="Could not create user")

    return {
        "first_name": user_obj.first_name,
        "last_name": user_obj.last_name,
        "username": user_obj.username,
        "time_until_birthday": calculate_time_until_birthday(user_obj.birth_date)
    }


@router.get("/users/{username}/", response_model=UserResponse)
async def get_user(username: str):
    user = await User.get_or_none(username=username)
    if not user:
        logger.warning(f"User not found: {username}")
        raise HTTPException(status_code=404, detail="User not found")

    logger.info(f"Fetched user: {username}")
    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "time_until_birthday": calculate_time_until_birthday(user.birth_date)
    }