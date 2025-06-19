from pydantic import BaseModel, Field
from typing import Optional, List


class VaccineSchema(BaseModel):
    name: str = Field(..., description="Name of the pill")
    vaccine_given_date: str = Field(..., description="Date when the vaccine was given")
    next_vaccine_date: Optional[str] = Field(None, description="Date when the next vaccine is due")
    pet_id: str = Field(..., description="ID of the pet to which the vaccine is administered")


class VaccineResponseSchema(BaseModel):
    status: str = Field(..., description="Status of the vaccine operation")
    message: str = Field(..., description="Message providing additional information")


class GetVaccinesResponseSchema(BaseModel):
    status: Optional[bool] = True
    message: str = Field(..., description="All vaccines for the specified pet")
    vaccines: List = Field(..., description="List of vaccines for the specified pet")
   
   