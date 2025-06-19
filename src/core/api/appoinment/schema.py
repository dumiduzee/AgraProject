from pydantic import BaseModel, Field
from typing import Optional,List


class AppointmentSchema(BaseModel):
    pet_id: str = Field(..., description="ID of the pet associated with the appointment")
    date: str = Field(..., description="Date of the appointment in YYYY-MM-DD format")
    time: str = Field(..., description="Time of the appointment in HH:MM format")
    title: str = Field(..., description="Reason for the appointment")
    location: str = Field(..., description="Location of the appointment") 

class AppointmentResponseSchema(BaseModel):
    id: str
    status:Optional[bool] = True
    message: Optional[str] = "Appointment created successfully"


class GetAppointmentResponseSchema(BaseModel):
    ststus: Optional[bool] = True
    message: Optional[str] = "Appointments retrieved successfully"
    appointments: List = Field(..., description="List of appointments for the specified pet")

class AppoinmentUpdateSchema(BaseModel):
    date: Optional[str] = Field(..., description="Updated date of the appointment in YYYY-MM-DD format")
    time: Optional[str] = Field(..., description="Updated time of the appointment in HH:MM format")
    title: Optional[str] = Field(..., description="Updated reason for the appointment")
    location: Optional[str] = Field(..., description="Updated location of the appointment")

class AppointmentUpdateResponseSchema(BaseModel):
    status: Optional[bool] = True
    message: Optional[str] = "Appointment updated successfully"