import pytest

from src.security import encode_password, decode_password


@pytest.mark.asyncio
async def test_encrytion():
    password1 = "supercomplexpassword123$456_"
    encoded1 = await encode_password(password1)
    decoded1 = await decode_password(encoded1)

    password2 = "supercomplexpassword123$456_7"
    encoded2 = await encode_password(password2)
    decoded2 = await decode_password(encoded2)

    assert decoded1 == password1
    assert decoded2 == password2
    assert encoded1 != encoded2
