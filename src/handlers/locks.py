from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from datetime import datetime
from uuid import UUID

from src.UserORM import UserORM
from src.ORM import session_maker


async def _update_locktime(user_id: UUID, value: datetime | None = datetime.now(), session: async_sessionmaker = session_maker) -> bool:
    try:
        async with session() as s:
            query = (
                update(UserORM).
                where(UserORM.id == user_id).
                values(locktime=value)
            )
            await s.execute(query)
            await s.commit()
            return True
    except SQLAlchemyError:
        return False


async def acquire_lock(user_id: UUID, session: async_sessionmaker = session_maker) -> bool:
    query = select(UserORM).where(UserORM.id == user_id)
    async with session() as s:
        query_result = await s.execute(query)
        user_locked_or_not_exists = True
        for user in query_result.scalars():
            if user.locktime is None:
                user_locked_or_not_exists = False
        if user_locked_or_not_exists:
            return False
        else:
            return await _update_locktime(user_id)


async def release_lock(user_id: UUID, session: async_sessionmaker = session_maker) -> bool:
    query = select(UserORM).where(UserORM.id == user_id)
    async with session() as s:
        query_result = await s.execute(query)
        user_exists = False
        for _ in query_result.scalars():
            user_exists = True
        if user_exists:
            return await _update_locktime(user_id, None)
        else:
            return False
