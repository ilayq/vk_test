import pytest

from src.handlers import create_user, get_users
from tests.env import Create_DB, UserRegisterDTO, Env, Domain, compare_users


@pytest.mark.asyncio
async def test_get_users():
    mock_db = Create_DB('test_get_users')
    users = [
        UserRegisterDTO(
            login='user1',
            password='password1',
            project_id='f461e285-585e-4655-b4ca-fcf73ef228ec',
            env=Env.PREPROD,
            domain=Domain.CANARY
        ),
        UserRegisterDTO(
            login='user2',
            password='password2',
            project_id='f461e285-585e-4655-b4ca-fcf73ef228ec',
            env=Env.PREPROD,
            domain=Domain.CANARY
        ),
        UserRegisterDTO(
            login='user3',
            password='password3',
            project_id='f461e285-585e-4655-b4ca-fcf73ef228ec',
            env=Env.PREPROD,
            domain=Domain.CANARY
        )
    ]

    async with mock_db:
        session_maker = mock_db.session_maker
        for user in users:
            await create_user(user, session_maker)
        for user, db_user in zip(users, await get_users(session_maker)):
            compare_users(user, db_user)