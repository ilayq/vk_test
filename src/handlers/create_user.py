from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.UserDTO import UserRegisterDTO
from src.UserORM import UserORM
from src.ORM import session


async def create_user(user: UserRegisterDTO, session: Session = session) -> None:
    try:
        async with session.begin() as s:
            user = UserORM(**user.model_dump())
            s.add(user)
        return True
    except SQLAlchemyError:
        return False
