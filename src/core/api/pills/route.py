from fastapi import APIRouter,Depends
from .schema import CreatePillSchema,CreatePillResponseSchema,GetPillsResponseSchema
from database.Superbase import Client, get_db
from typing import Annotated
from .service import create_pill_service,get_pills_service

router = APIRouter(tags=["Pills"])


@router.get("/{pet_id}", description="Get all pills for a pet",response_model=GetPillsResponseSchema)
def getPills(pet_id: str, db: Annotated[Client, Depends(get_db)]):
    return GetPillsResponseSchema(
        pills=get_pills_service(pet_id, db),
        status=True,
        message="Pills retrieved successfully"
    )




# # Create a new pill for pet
@router.post("/create", description="Use for create new pill for pet",response_model=CreatePillResponseSchema)
def create_pill(pill:CreatePillSchema, db: Annotated[Client, Depends(get_db)]):
    response = create_pill_service(pill.model_dump(), db)
    return CreatePillResponseSchema(id=response.get("id"))