import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


SECRET_KEY = os.getenv("SECRET_KEY")
ADMIN_LOGIN = os.getenv("ADMIN_LOGIN")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def get_key(password: str) -> bytes:
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password.encode())
    return base64.urlsafe_b64encode(digest.finalize())


SECRET_KEY = get_key(SECRET_KEY)

f = Fernet(SECRET_KEY)
