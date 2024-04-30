import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


SECRET_KEY = os.getenv("SECRET_KEY")
ADMIN_LOGIN = os.getenv("ADMIN_LOGIN")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


if not (SECRET_KEY and ADMIN_LOGIN and ADMIN_PASSWORD):
    raise ValueError("Provide SECRET_KEY, ADMIN_LOGIN, ADMIN_PASSWORD as env variables") 


def get_key(password: str) -> bytes:
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password.encode())
    return base64.urlsafe_b64encode(digest.finalize())


f = Fernet(get_key(SECRET_KEY))
