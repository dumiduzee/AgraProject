from fastapi import APIRouter,Depends,File,UploadFile,Form,status
from typing import Annotated
from database.Superbase import Client,get_db
from .schema import RegisterPetSchema,RegisterPetResponse,DeletePetResponse,GetPetResponse
from .service import petRegisterService,DeletePetService,GetPetsByOwnerId



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
    

#Delete pet with pet id
@router.delete("/{pet_id}",description="Use for delete pet from the system",status_code=status.HTTP_200_OK,response_model=DeletePetResponse)
async def deletePet(pet_id:str,db:Annotated[Client,Depends(get_db)]):
    """
    Delete a pet from the system using its ID.
    
    Args:
        pet_id (str): The ID of the pet to be deleted.
        db (Client): The database client dependency.
    
    Returns:
        None: If the deletion is successful, returns no content.
    """
    # Here you would typically add logic to delete the pet from the database
    # For now, we will just return a 204 No Content response
    deleted_petid = DeletePetService(pet_id, db)
    return DeletePetResponse(
        message="Pet deleted successfully",
        pet_id=deleted_petid)


#Get pet from owner id
@router.get("/{owner_id}",description="Use for get all pets of owner",status_code=status.HTTP_200_OK,response_model=GetPetResponse)
async def getPetsByOwnerId(owner_id:str,db:Annotated[Client,Depends(get_db)]):
    """
    Get all pets of an owner by owner ID.
    
    Args:
        owner_id (str): The ID of the owner whose pets are to be retrieved.
        db (Client): The database client dependency.
    
    Returns:
        List[Pet]: A list of pets owned by the specified owner.
    """
    response = GetPetsByOwnerId(owner_id, db)
    return GetPetResponse(
        message="Pets retrieved successfully",
        pets=response
    )