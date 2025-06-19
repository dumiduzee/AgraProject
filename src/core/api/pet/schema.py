from pydantic import BaseModel,Field
from typing import Annotated,Optional,List
from datetime import date
from enum import Enum

class PetGender(Enum):
    male = "Male"
    female = "Female"

class RegisterPetSchema(BaseModel):
    petName:Annotated[str,Field(min_length=3)]
    petAge:Annotated[int,Field(min=1,max=100)]
    petBirthday:date
    petGender:PetGender
    petColor:str
    petBread:str
    owner_id:str

class RegisterPetResponse(BaseModel):
    status:Optional[bool] = True
    message:str
    pet_id:str

class DeletePetResponse(BaseModel):
    status:Optional[bool] = True
    message:str
    pet_id:str

class GetPetResponse(BaseModel):
    status:Optional[bool] = True
    message:str
    pets: list = Field(default_factory=list)
   
    

