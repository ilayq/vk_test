from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date

from .Enums import Env, Domain


class UserRegisterDTO(BaseModel):
    login: str
    password: str
    project_id: UUID
    env: Env
    domain: Domain


class UserDTO(BaseModel):
    id: UUID
    created_at: date
    login: str
    password: str
    project_id: UUID
    env: Env
    domain: Domain
    locktime: datetime | None

    class Config:
        from_attributes = True
