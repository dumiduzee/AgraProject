from fastapi import File
import os
from .utils import GenarateUniueNameForProfilePicture,CloudinaryUpload
from .exceptions import ContentTypeNotValidException
from .repository import InsertPet
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
    return InsertPet(petData,db=db)[0]["id"]
    
