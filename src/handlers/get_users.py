from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.ORM import session_maker
from src.UserORM import UserORM
from src.UserDTO import UserDTO
from src.security import decode_password


async def get_users(session: async_sessionmaker = session_maker) -> list[UserDTO]:
    result = []
    query = select(UserORM)
    async with session.begin() as s:
        query_result = await s.execute(query)
        for user in query_result.scalars():
            userdto = UserDTO.model_validate(user, strict=True, from_attributes=True)
            userdto.password = await decode_password(userdto.password)
            result.append(userdto)

    return result
