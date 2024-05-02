import pytest

from tests.env import Create_DB
from src.handlers import create_user, get_users, acquire_lock, release_lock


@pytest.mark.asyncio
async def test_acquire_lock():
    db = Create_DB('test_release_lock')
    async with db:
        user, session_maker = db.mock_user, db.session_maker
        await create_user(user, session_maker)
        db_user = (await get_users(session_maker))[0]
        await acquire_lock(db_user.id, session_maker)
        assert await release_lock(db_user.id, session_maker)
        db_user = (await get_users(session_maker))[0]
        assert not db_user.locktime
