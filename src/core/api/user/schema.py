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

class UpdateUserSchema(BaseModel):
    username: str = Field(...,min_length=3,description="Must need valid registerd firebase userid")

class UpdateUserResponseSchema(BaseModel):
    status:Optional[bool] = True
    message:str