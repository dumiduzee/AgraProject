from fastapi import HTTPException


class UserExceptions(HTTPException):
    pass


class UserRegistrationException(UserExceptions):
    def __init__(self, detail: str = "User registration failed."):
        super().__init__(status_code=400, detail=detail)
        self.solution = "Please check the user details and try again."


class UpdateUserExceptions(UserExceptions):
    def __init__(self,detail:str = "Error while updating user"):
        super().__init__(status_code=400, detail=detail)
        self.solution = "Try again sometime"