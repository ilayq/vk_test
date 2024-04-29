from fastapi import FastAPI, Response, HTTPException
import uvicorn
from uuid import UUID

from src.UserDTO import UserDTO, UserRegisterDTO
import src.handlers as handlers


app = FastAPI()


@app.get('/healthcheck')
async def healthcheck():
    return Response(status_code=200)


@app.get('/get_users')
async def get_users() -> list[UserDTO]:
    return await handlers.get_users()


@app.post('/create_user')
async def create_user(user: UserRegisterDTO) -> Response:
    result = await handlers.create_user(user)
    if result:
        return Response(status_code=200)
    raise HTTPException(status_code=409, detail="User already exists")


@app.get('/acquire_lock')
async def acquire_lock(id: UUID) -> Response:
    if await handlers.acquire_lock(id):
        return Response(status_code=200)
    raise HTTPException(status_code=409, detail="User is locked or not exists")


@app.get('/release_lock')
async def release_lock(id: UUID) -> Response:
    if await handlers.release_lock(id):
        return Response(status_code=200)
    raise HTTPException(detail="User doesn`t exist", status_code=409)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
