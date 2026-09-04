from passlib.context import CryptContext
from jose import jwt, JWTError


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


SECRET_KEY = "my-secret-key"

ALGORITHM = "HS256"


def create_access_token(data):

    print("CREATE SECRET:", SECRET_KEY)

    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def verify_access_token(token):

    try:
        print("VERIFY SECRET:", SECRET_KEY)

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("JWT PAYLOAD:", payload)

        return payload

    except JWTError as e:
        print("JWT ERROR:", e)

        return None