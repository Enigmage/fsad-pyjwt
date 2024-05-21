from cryptography.hazmat.primitives import serialization
import jwt


public_pem = b"""
 -----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr3N+k+FLxkja0JWgeASc
dzW3MawobHWDAWOq1lp9+6peznuEqK2CJIaFBIcN/OjRBDbAS2jIlqioS/ynieFO
3wp/8j0d24TJaPMA6xzB+SqeKfcHDa5sMd89nFThi6efi1jMOLMAs1zRu1S6tceQ
9sSgkKFt8sssJhVb8Co66YgW/OOzH8WmFH2onxUEGFWo9W0H1DkrMac47zGhq0CW
eGTUtYUzSH/E3I3AltZ0gEReK5v4ZSN1EiiUrs/hi3kGW7iC9OxattE+buZENHHT
kDseUFKvypiOiHrgbdJG0t73VZkePKDYEs4c9//UfsWYMtJUAqKy3f0OyzyC4Aiw
8QIDAQAB
-----END PUBLIC KEY-----
"""

encoded_jwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFsaXphaWRpIiwidXNlcklEIjo5OTksImV4cCI6MTcxNjI3NzcwM30.htd5_-X_Z3cG2ikhZSVB-Z6WyEPu_JxVAmu0OlMOfy486zo_tdRmiX_ZFPM3ogIo7Zmzo7I-oFOmUA7Pm6_KiiJXy0GcRcuKogZJ1A_poSH_gN5sbUU7QK4UL1Suya0Ojvxu89rNHdMGyciXt00cfd67w3rXZVaKkWNEAveA-nz12ALt5scW8Fwep53e69Z2mCoBn5ZJ0U-JK6dz4L8RSpdTsUFdo9qYdSHpSlpd4IZrKIY92fWu1kPaPrSMyc79tBwquqUFidrGrj5ZSw5osbDiOmCJF9nkCVTwi43AJQ-rejsYboCjkEpquXRlggxvUTJ-EpqJEqimdkyDvc_cSA"

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
