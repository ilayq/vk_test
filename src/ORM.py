from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os


db_user = os.getenv('POSTGRES_USER')
db_user_password = os.getenv('POSTGRES_PASSWORD')
host = os.getenv('HOST') or 'localhost'
db_name = os.getenv('POSTGRES_DB') or 'vk_test'
db_connection_string = f'postgresql+asyncpg://{db_user}:{db_user_password}@{host}:5432/{db_name}'
engine = create_async_engine(db_connection_string)
session_maker = async_sessionmaker(engine)
