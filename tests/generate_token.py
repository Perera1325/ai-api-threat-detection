from jose import jwt

SECRET = "supersecretkey"
ALGORITHM = "HS256"

payload = {
    "user":"test-user"
}

token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)

print("JWT TOKEN:")
print(token)