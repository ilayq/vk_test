from sqlalchemy import select
from sqlalchemy.orm import Session

from src.ORM import session
from src.UserORM import UserORM
from src.UserDTO import UserDTO
from src.security import decode_password


async def get_users(session: Session = session) -> list[UserDTO]:
    result = []
    query = select(UserORM)
    async with session.begin() as s:
        query_result = await s.execute(query)
        for user in query_result.scalars():
            userdto = UserDTO.model_validate(user, strict=True, from_attributes=True)
            userdto.password = decode_password(userdto.password)
            result.append()

    return result