from time import time
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

from .security_config import ADMIN_LOGIN, ADMIN_PASSWORD, SECRET_KEY, f


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="admin/login")


async def make_auth_token(username: str, password: str) -> str:
    return f.encrypt(f'{username}|{password}|{time()}'.encode()).decode()


async def check_auth_token(token: Annotated[str, Depends(oauth2_scheme)]) -> bool:
    username, password, _ = f.decrypt(token.encode()).decode().split('|')
    return username == ADMIN_LOGIN and password == ADMIN_PASSWORD
