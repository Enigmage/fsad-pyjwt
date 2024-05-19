from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import jwt
import time

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key = private_key.public_key()
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

print("Public Key (PEM format):\n", public_pem.decode())
print("\nPrivate Key (PEM format):\n", private_pem.decode())

payload = {
    "username": "alizaidi",
    "userID": 999,
    "exp": int(time.time()) + 60 * 60,
}

encoded_jwt = jwt.encode(payload, private_pem, algorithm="RS256")

print("\nEncoded JWT:\n", encoded_jwt)
