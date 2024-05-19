import os
from dotenv import load_dotenv
import jwt

load_dotenv()
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFsaXphaWRpIiwidXNlcklEIjo5OTksImV4cCI6MTcxNjExNjcxMX0.LClm5Zyb-Coo6ADlw2sz-K18-JTkqC-5v-VQATG4T_Y"

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
