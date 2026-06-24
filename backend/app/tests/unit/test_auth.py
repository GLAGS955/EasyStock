from app.core.security import create_access_token, decode_token, get_password_hash, verify_password


def test_password_hash_and_verify():
    hashed = get_password_hash("password123")
    assert verify_password("password123", hashed)
    assert not verify_password("wrong", hashed)


def test_create_and_decode_token():
    token = create_access_token(subject="user@test.com")
    assert decode_token(token) == "user@test.com"


def test_decode_invalid_token():
    assert decode_token("invalid.token") is None
