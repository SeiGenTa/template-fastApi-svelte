from pydantic import BaseModel

class RegisterUser(BaseModel):
    username: str
    email: str
    password: str

class LoginUser(BaseModel):
    username: str
    password: str
    
class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    new_password: str | None = None
    first_name: str | None = None
    last_name: str | None = None