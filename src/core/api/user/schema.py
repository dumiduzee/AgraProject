from pydantic import BaseModel, Field
from typing import Optional


class RegisterUserRequest(BaseModel):
    username: str
    email: str
    user_id:str

class RegisterUserResponse(BaseModel):
    user_id: str
    username: str
    email: str