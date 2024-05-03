from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from src.UserDTO import UserRegisterDTO
from src.UserORM import UserORM
from src.ORM import session_maker
from src.security import encode_password


async def create_user(user: UserRegisterDTO, sm: async_sessionmaker = session_maker) -> bool:
    try:
        async with sm() as session:
            async with session.begin():
                user = UserORM(**user.model_dump())
                user.env = user.env.value
                user.domain = user.domain.value
                user.password = await encode_password(user.password)
                session.add(user)
        return True
    except SQLAlchemyError as e:
        print(e)
        return False
