from pydantic import BaseModel, Field
from typing import Optional


class RegisterUserRequest(BaseModel):
    username: str
    email: str
    user_id:str

class RegisterUserResponse(BaseModel):
    status:Optional[bool] = True
    user_id: str
    username: str
    email: str