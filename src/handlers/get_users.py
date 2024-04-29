from sqlalchemy import select
from sqlalchemy.orm import Session

from src.ORM import session
from src.UserORM import UserORM
from src.UserDTO import UserDTO

async def get_users(session: Session = session) -> list[UserDTO]:
    result = []
    query = select(UserORM)
    async with session.begin() as s:
        query_result = await s.execute(query)
        for user in query_result.scalars():
            result.append(UserDTO.model_validate(user, strict=True, from_attributes=True))
    return result