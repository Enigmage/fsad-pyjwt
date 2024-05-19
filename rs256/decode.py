from cryptography.hazmat.primitives import serialization
import jwt


public_pem = b"""
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArWBx8U8P2fkkyTNxGLqa
GiIUkjsgGyPpLzocV8mVUa5eaTuoB2A4NUz6BSg/Ka5zMq2vSIBymRsOXe8nAV5e
0SbMjyZnpP1Igw0z5sgi75au6inbc9FW1kkbRzd75FCATq6CC6VqtUoe3m/yDIr5
yXmCATN2inH6cZx6Ne/ZzkwDMAie7gK5nDDk2+2TRg6AbPZeQx6srrux7dEe8FJf
Nt7+xs4CFfou8GSngsS++c5H1hY+E7gEYeaX3mRUUOOPtjGH0yhRufukKpVew5Bg
jDNkoEGH377o3vZjK7iBfJpFP9p0rU1EvbgoiAmYFmG+bDZLmMgdmsLK/4B0h+vx
nwIDAQAB
-----END PUBLIC KEY-----
"""

encoded_jwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFsaXphaWRpIiwidXNlcklEIjo5OTksImV4cCI6MTcxNjExNzk5OH0.kQEQxEkNQX0_fRa4oTjFNrxUuxGbJM7QAnagesGF-nvFfWdt5nbbnrzsgWimWrkSeIdR3d-FUCPJMhw2ylrHIt3cvMksUaZmNZAAKfO_gaCZOsvKK_w3VnGWkQrx6NihI4f4BZGJ5sUp1MO8pFqgckjOqKluFo9lBgo-Soc9bnEeqT_h7NfwgJgS54ubUOmBLarsdAjRpAUqbJ5l5e15mVvBf55UZHyavXVa1QykILsOeAKRXZrguyAZLYs5o6RjDQnrAALbdslo5QEHC5AByNxibXjcA_TG_2Q6Gz2WSGmRQyvh_j5c7ChUhm_scS8eohRRPGVnBSkdk6pF3VioyQ"

try:
    decoded = jwt.decode(encoded_jwt, public_pem, algorithms=["RS256"])
    print("Decoded JWT:\n", decoded)
except jwt.exceptions.ExpiredSignatureError:
    print("Token has expired.")
except jwt.exceptions.InvalidTokenError as e:
    print("Invalid token:", e)
except jwt.exceptions.PyJWTError as e:
    print("Error decoding token:", e)
except Exception as e:
    print("Unexpected error:", e)
