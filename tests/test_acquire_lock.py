import pytest

from tests.env import CreateDB
from src.handlers import create_user, get_users, acquire_lock


@pytest.mark.asyncio
async def test_acquire_lock():
    db = CreateDB('test_acquire_lock')
    async with db:
        user, session_maker = db.mock_user, db.session_maker
        await create_user(user, session_maker)
        db_user = (await get_users(session_maker))[0]
        assert db_user.id
        assert not db_user.locktime
        assert await acquire_lock(db_user.id, session_maker)
        db_user = (await get_users(session_maker))[0]
        assert db_user.locktime

        assert not await acquire_lock(db_user.id, session_maker)
