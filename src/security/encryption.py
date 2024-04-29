from .security_config import f


async def encode_password(password: str) -> str:
    return f.encrypt(password.encode()).decode()


async def decode_password(encoded_password: str) -> str:
    return f.decrypt(encoded_password.encode()).decode()
