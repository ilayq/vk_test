from sqlalchemy import select, update
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from datetime import datetime
from uuid import UUID

from src.UserORM import UserORM
from src.ORM import session


async def _update_locktime(id: UUID, value: datetime = datetime.now(), session: Session = session) -> bool:
    try:
        async with session.begin() as s:
            query = (
                update(UserORM).
                where(UserORM.id == id).
                values(locktime=value)
            )
            await s.execute(query)
            return True
    except SQLAlchemyError:
        return False


async def acquire_lock(id: UUID, session: Session = session) -> bool:
    query = select(UserORM).where(UserORM.id == id)
    async with session.begin() as s:
        query_result = await s.execute(query)
        user_locked_or_not_exists = True
        for user in query_result.scalars():
            if user.locktime is None:
                user_locked_or_not_exists = False
        if user_locked_or_not_exists:
            return False
        else:
            return await _update_locktime(id)


async def release_lock(id: UUID, session: Session = session) -> bool:
    query = select(UserORM).where(UserORM.id == id)
    async with session.begin() as s:
        query_result = await s.execute(query)
        user_exists = False
        for _ in query_result.scalars():
            user_exists = True
        if user_exists:
            return await _update_locktime(id, None)
        else:
            return False
