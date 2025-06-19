import uuid
import cloudinary.uploader
from config.cloudinary import cloudinary
from .exceptions import CloudinaryUploadException

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
