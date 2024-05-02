import pytest

import os
from src.security import make_auth_token, check_auth_token


@pytest.mark.asyncio
async def test_decode_token():
    username = os.getenv('ADMIN_LOGIN')
    password = os.getenv('ADMIN_PASSWORD')
    token = await make_auth_token(username, password)
    decoded_token = await check_auth_token(token)
    assert decoded_token
