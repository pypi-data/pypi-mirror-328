from pydantic import BaseModel

class AuthToken(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AuthUser(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool = False 