import pytest
from src.handlers import create_user, get_users
from tests.env import CreateDB, compare_users


@pytest.mark.asyncio
async def test_create_unique_user():
    mock_db = CreateDB('test_create_user')
    async with mock_db:
        mock_user, session_maker = mock_db.mock_user, mock_db.session_maker
        await create_user(mock_user, session_maker)
        users = await get_users(session_maker)
        assert len(users) == 1
        compare_users(mock_user, users[0])

        assert not await create_user(mock_user, session_maker)
