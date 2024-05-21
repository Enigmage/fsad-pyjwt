import os
from dotenv import load_dotenv
import jwt

load_dotenv()
token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFsaXphaWRpIiwidXNlcklEIjo5OTksImV4cCI6MTcxNjI4MTczM30.ldTp3O22pEwwBWI-s3CpInSYXYalZ-cU_xfKp_R89HeRdyqgpz8_nnD8GB470gJvR8TKLKCGoArpL5TaLrZJhQ"

secret = os.getenv("SECRET_KEY")


try:
    if token and secret:
        decoded = jwt.decode(token, secret, algorithms=["HS512"])
        print(decoded)
    else:
        print("Token or secret key not found.")
except jwt.exceptions.ExpiredSignatureError:
    print("Token has expired.")
except jwt.exceptions.DecodeError:
    print("Invalid token.")
except Exception as e:
    print("Error:", e)
