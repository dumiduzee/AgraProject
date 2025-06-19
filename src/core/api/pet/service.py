from fastapi import File
import os
from .utils import GenarateUniueNameForProfilePicture,CloudinaryUpload,sendSms
from .exceptions import ContentTypeNotValidException
from .repository import InsertPet,DeletePet,GetPet
from datetime import date
from enum import Enum


#Register pet service to handle pet data
def petRegisterService(image,petData,db):
    #chedk if image is valid type
    print("content",image.content_type)
    if image.content_type != "image/jpeg" and image.content_type !=  "image/png" and image.content_type !=  "image/jpg":
        #if image type wrong raise exception
        raise ContentTypeNotValidException()
    #genarate unique file name
    file_name = GenarateUniueNameForProfilePicture(os.path.splitext(image.filename)[0])
    imageUrl = CloudinaryUpload(image,file_name,"pet_profile")
    petData["profile_pic"] = imageUrl
    #check pet birthday is type of date
    if isinstance(petData["petBirthday"],date):
        petData["petBirthday"] = petData["petBirthday"].isoformat()
    #check genter is instance of Enum
    if isinstance(petData["petGender"],Enum):
        petData["petGender"] = petData["petGender"].value
    #Insert petinto database
    sendSms(petName=petData["petName"])
    return InsertPet(petData,db=db)[0]["id"]

#Delete pet service to handle pet deletion
def DeletePetService(pet_id, db):
    """
    Delete a pet from the system using its ID.
    
    Args:
        pet_id (str): The ID of the pet to be deleted.
        db (Client): The database client dependency.
    
    Returns:
        None: If the deletion is successful, returns no content.
    """
    response = DeletePet(pet_id, db)
    return response[0]["id"]


#get pet by owner id
def GetPetsByOwnerId(owner_id, db):
    """
    Get all pets of an owner by owner ID.
    
    Args:
        owner_id (str): The ID of the owner whose pets are to be retrieved.
        db (Client): The database client dependency.
    
    Returns:
        List[Pet]: A list of pets owned by the specified owner.
    """
    response = GetPet(owner_id, db)
    return response
    
    
