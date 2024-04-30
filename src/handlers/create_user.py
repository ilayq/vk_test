from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.UserDTO import UserRegisterDTO
from src.UserORM import UserORM
from src.ORM import session
from src.security import encode_password


async def create_user(user: UserRegisterDTO, session: Session = session) -> None:
    try:
        async with session.begin() as s:
            user = UserORM(**user.model_dump())
            user.password = await encode_password(user.password)
            s.add(user)
        return True
    except SQLAlchemyError as e:
        print(e)
        return False
