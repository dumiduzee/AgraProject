import uuid
import cloudinary.uploader
from config.cloudinary import cloudinary
from .exceptions import CloudinaryUploadException
import requests
from decouple import config

#Genarate random name for pet profile picture
def GenarateUniueNameForProfilePicture(fileName):
    """When supply file name it genarate random uniqu file name wih uuid"""
    return f"pet_images/{uuid.uuid4()}_{fileName}"

#Upload image for cloudinary
def CloudinaryUpload(file,fileId,folder):
    """Upload image to cloudinary"""
    try:
        result = cloudinary.uploader.upload(
            file=file.file,
            public_id=fileId,
            folder=folder,
            overwrite=True,
            resource_type="image"
        )
        return result["url"]
    except Exception:
        raise CloudinaryUploadException
    



#Sms api

def sendSms(petName):
    number = config("SMS_NUMBER")
    print("number", number)
    if number == "":
        return
    params = {
        "user_id":config("USER_ID"),
        "api_key":config("TEXT_SMS_API"),
        "sender_id":config("SENDER_ID"),
        "to":number,
        "message":f"New Pet Added Successfully. {petName} is now part of your family. Enjoy your time with {petName}!",
    }

    response = requests.post(config("TEXT_SMS_URL"), data=params)
    print(response)
