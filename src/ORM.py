from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os


db_user = os.getenv('POSTGRES_USER')
db_user_password = os.getenv('POSTGRES_PASSWORD')
host = os.getenv('HOST') or 'postgres'
db_name = os.getenv('DB_NAME') or 'vk_test'
db_connection_string = f'postgresql+asyncpg://{db_user}:{db_user_password}@{host}:5432/{db_name}'

engine = create_async_engine(db_connection_string)
session = async_sessionmaker(engine)
