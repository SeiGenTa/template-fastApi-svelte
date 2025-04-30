import os
from dotenv import load_dotenv

load_dotenv()

secret_jwt = os.getenv("SECRET_JWT", "secretJWT")
secret_revalidate_jwt = os.getenv("SECRET_REVALIDATE_JWT", "secretRevalidateJWT")
