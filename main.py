from fastapi import FastAPI, Response, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
import uvicorn

from uuid import UUID
from typing import Annotated

from src.UserDTO import UserDTO, UserRegisterDTO
import src.handlers as handlers
from src.security import check_auth_token, make_auth_token, security_config


app = FastAPI()


@app.get('/healthcheck')
async def healthcheck():
    return Response(status_code=200)


@app.get('/get_users')
async def get_users(is_logged: Annotated[bool, Depends(check_auth_token)]) -> list[UserDTO]:
    return await handlers.get_users()


@app.post('/create_user')
async def create_user(user: UserRegisterDTO, is_logged: Annotated[bool, Depends(check_auth_token)]) -> Response:
    result = await handlers.create_user(user)
    if result:
        return Response(status_code=200)
    raise HTTPException(status_code=409, detail="User already exists")


@app.get('/acquire_lock')
async def acquire_lock(user_id: UUID, is_logged: Annotated[bool, Depends(check_auth_token)]) -> Response:
    if await handlers.acquire_lock(user_id):
        return Response(status_code=200)
    raise HTTPException(status_code=409, detail="User is locked or not exists")


@app.get('/release_lock')
async def release_lock(user_id: UUID, is_logged: Annotated[bool, Depends(check_auth_token)]) -> Response:
    if await handlers.release_lock(user_id):
        return Response(status_code=200)
    raise HTTPException(detail="User doesn`t exist", status_code=409)


@app.post('/admin/login')
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    username, password = form_data.username, form_data.password
    if security_config.ADMIN_LOGIN != form_data.username or security_config.ADMIN_PASSWORD != form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": await make_auth_token(username, password), "token_type": "bearer"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
