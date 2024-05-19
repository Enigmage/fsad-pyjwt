import os
import jwt
import time
from dotenv import load_dotenv


load_dotenv()

# Secret key (replace with your own)
secret = os.getenv("SECRET_KEY")

# Payload
payload = {
    "username": "alizaidi2",
    "userID": 231,
    "exp": int(time.time()) + 60 * 60,  # Add expiration time (1 hour)
}

# Generate JWT
if secret:
    token = jwt.encode(payload, secret, algorithm="HS256")

    print(token)
