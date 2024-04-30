from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from src.UserDTO import UserRegisterDTO
from src.UserORM import UserORM
from src.ORM import session_maker
from src.security import encode_password


async def create_user(user: UserRegisterDTO, session: async_sessionmaker = session_maker) -> bool:
    try:
        async with session.begin() as s:
            user = UserORM(**user.model_dump())
            user.password = await encode_password(user.password)
            s.add(user)
        return True
    except SQLAlchemyError:
        return False
