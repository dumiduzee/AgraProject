from fastapi import APIRouter,Depends
from .schema import VaccineSchema,VaccineResponseSchema,GetVaccinesResponseSchema
from database.Superbase import Client,get_db
from typing import Annotated
from .service import create_vaccine_service,get_vaccines_service

router = APIRouter(tags=["Vaccine"])

#get all vaciens
@router.get("/{pet_id}",description="Get all vaccines for a pet",response_model=GetVaccinesResponseSchema)
def getVaccines(pet_id: str, db: Annotated[Client, Depends(get_db)]):
    response = get_vaccines_service(pet_id, db)
    if response:
        return GetVaccinesResponseSchema(status=True, message="Vaccines retrieved successfully", vaccines=response)
    return GetVaccinesResponseSchema(status=True, message="No vaccines found for this pet", vaccines=[])


# create new vaccine
@router.post("/create",description="Create a new vaccine",response_model=VaccineResponseSchema)
def create_vaccine(vaccine:VaccineSchema,db:Annotated[Client, Depends(get_db)]):
    response = create_vaccine_service(vaccine.model_dump(), db)
    if response:
        return VaccineResponseSchema(status="success", message="Vaccine created successfully")
    return VaccineResponseSchema(status="error", message="Failed to create vaccine")
