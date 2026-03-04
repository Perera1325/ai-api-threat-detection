from jose import jwt

SECRET = "supersecretkey"
ALGORITHM = "HS256"

API_KEYS = [
    "123456",
    "abcdef"
]

def validate_api_key(key):

    if key in API_KEYS:
        return True

    return False


def validate_jwt(token):

    try:

        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])

        return payload

    except Exception:

        return None