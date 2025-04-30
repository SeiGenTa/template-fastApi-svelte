import datetime
import jwt
from src.config import secret_jwt

db_temp:list["User"] = []


class User:
    """User model for the application.

    Attributes:
        _id (str): Unique identifier for the user.
        username (str): Username of the user.
        email (str): Email address of the user.
        hash_password (str): Hashed password of the user.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        is_active (bool): Indicates if the user is active or not.
    """

    def __init__(self, username: str, email: str, hash_password: str) -> "User":
        self._id: str = None
        self.username: str = username
        self.email: str = email
        self.hash_password: str = hash_password
        self.first_name: str = None
        self.last_name: str = None
        self.is_active: bool = True

    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"

    @staticmethod
    def fromJson(data: dict) -> "User":
        user = User(
            username=data.get("username"),
            email=data.get("email"),
            hash_password=data.get("hash_password"),
        )
        user._id = data.get("_id")
        user.first_name = data.get("first_name")
        user.last_name = data.get("last_name")
        user.is_active = data.get("is_active", True)
        return

    def toJson(self) -> dict:
        return {
            "_id": self._id,
            "username": self.username,
            "email": self.email,
            "hash_password": self.hash_password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active,
        }

    def generate_jwt(self) -> tuple[str, str, datetime.datetime, datetime.datetime]:
        json = {
            "type": "jwt",
            "id": self._id,
            "username": self.username,
            "email": self.email,
            "exp": datetime.datetime.now() + datetime.timedelta(days=1),  # Token expiration time in seconds
        }
        json_revalidate = {
            "type": "revalidate_jwt",
            "id": self._id,
            "username": self.username,
            "email": self.email,
            "exp": datetime.datetime.now() + datetime.timedelta(days=30),  # Token expiration time in seconds
        }

        token = jwt.encode(json, secret_jwt, algorithm="HS256")
        token_revalidate = jwt.encode(json_revalidate, secret_jwt, algorithm="HS256")
        return token, token_revalidate, json["exp"], json_revalidate["exp"]
    
    def save(self) -> None:
        """Save the user to the database (temporary in-memory list)."""
        self._id = str(len(db_temp) + 1)
        db_temp.append(self)
        print(f"User {self.username} saved with ID {self._id}")
    
    @staticmethod
    def get_user_from_jwt(token: str) -> dict:
        try:
            decoded = jwt.decode(token, secret_jwt, algorithms=["HS256"])
            return decoded
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
        except Exception as e:
            print(f"Error decoding JWT: {e}")
            return None