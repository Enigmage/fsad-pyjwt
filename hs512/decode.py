import os
from dotenv import load_dotenv
import jwt

load_dotenv()
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFsaXphaWRpIiwidXNlcklEIjo5OTksImV4cCI6MTcxNjI3NzM3OX0.Yf0c3Msf7MQTCU2IHC5v5t1oxRsjrCX0CH2vDK-pT9g"

secret = os.getenv("SECRET_KEY")


try:
    if token and secret:
        decoded = jwt.decode(token, secret, algorithms=["HS256"])
        print(decoded)
    else:
        print("Token or secret key not found.")
except jwt.exceptions.ExpiredSignatureError:
    print("Token has expired.")
except jwt.exceptions.DecodeError:
    print("Invalid token.")
except Exception as e:
    print("Error:", e)
