from pydantic import BaseModel, Field
from typing import Optional, List


class CreatePillSchema(BaseModel):
    name: str = Field(..., description="Name of the pill")
    time: Optional[str] = Field(None, description="Description of the pill")
    pet_id: str = Field(..., description="Dosage of the pill")

class CreatePillResponseSchema(BaseModel):
    id: str
    status: Optional[bool] = True
    message: Optional[str] = "Pill added successfully"

class GetPillsResponseSchema(BaseModel):
    status: Optional[bool] = True
    message: Optional[str] = "Pills retrieved successfully"
    pills: List = Field(..., description="List of pills for the pet")