from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import asyncpg

from src.UserORM import Base
from src.Enums import Env, Domain
from src.ORM import db_user, db_user_password, host
from src.UserDTO import UserRegisterDTO


class CreateDB:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.con_string = f"postgresql+asyncpg://{db_user}:{db_user_password}@{host}/{db_name}"
        self.engine = create_async_engine(self.con_string)
        self.session_maker = async_sessionmaker(self.engine)

        self.mock_user = UserRegisterDTO(
                            login='user',
                            password='password',
                            project_id='4324d5f3-a631-4102-9fd0-739f68c73903',
                            env=Env.PREPROD,
                            domain=Domain.REGULAR
                        )

    async def __aenter__(self):
        self.con = await asyncpg.connect(
            user=db_user,
            password=db_user_password,
            host=host,
            database='template1'
        )
        await self.con.execute(f"CREATE DATABASE {self.db_name}")

        async with self.engine.begin() as db:
            await db.run_sync(Base.metadata.drop_all)
            await db.run_sync(Base.metadata.create_all)
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.con.execute(f"select pg_terminate_backend(pid) from pg_stat_activity where datname='{self.db_name}'")
        await self.con.execute(f"DROP DATABASE {self.db_name}")
        await self.con.close()


def compare_users(original: UserRegisterDTO, new):
    for attr, value in original.__dict__.items():
        assert value == new.__dict__[attr]
