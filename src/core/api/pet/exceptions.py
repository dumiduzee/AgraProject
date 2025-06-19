from fastapi import HTTPException

class PetExceptions(HTTPException):
    pass

class ContentTypeNotValidException(PetExceptions):
    def __init__(self, status_code:int=401, detail:str = "Content type not valid",solution:str="Make sure you uploaded the correct file format"):
        super().__init__(status_code, detail)
        self.solution = solution


class CloudinaryUploadException(PetExceptions):
    def __init__(self, status_code=505, detail = "Internal server error"):
        super().__init__(status_code=status_code, detail=detail,)
        self.solution = "Try again later"