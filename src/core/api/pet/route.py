from fastapi import APIRouter,Depends,File,UploadFile,Form,status
from typing import Annotated
from database.Superbase import Client,get_db
from .schema import RegisterPetSchema,RegisterPetResponse
from .service import petRegisterService



router = APIRouter(tags=["Pet"])

#Register pet to the system
@router.post("/",description="Use for register new pet to the system",response_model=RegisterPetResponse,status_code=status.HTTP_201_CREATED)
async def registerPet(file:UploadFile,pet_data: Annotated[RegisterPetSchema, Depends()],db:Annotated[Client,Depends(get_db)]):
    #pass pet data to service layer
    pet_id = petRegisterService(file,pet_data.model_dump(),db)
    return RegisterPetResponse(
        message="Pet added to the database",
        pet_id=pet_id
    )
    
