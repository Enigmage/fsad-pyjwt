import os
import jwt
import time
from dotenv import load_dotenv


load_dotenv()

secret = os.getenv("SECRET_KEY")

payload = {
    "username": "alizaidi",
    "userID": 999,
    "exp": int(time.time()) + 60 * 60,
}

if secret:
    token = jwt.encode(payload, secret, algorithm="HS512")

    print(token)
