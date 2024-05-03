from sqlalchemy import Column, Date, String, TIMESTAMP, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4


Base = declarative_base()


class UserORM(Base):
    __tablename__ = 'useraccount'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at = Column(Date, server_default=func.now(), nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    project_id = Column(UUID(as_uuid=True), default=uuid4, nullable=False)
    env = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    locktime = Column(TIMESTAMP, default=None)
