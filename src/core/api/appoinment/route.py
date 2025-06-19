from fastapi import APIRouter


router = APIRouter(tags=["Appoinment"])


@router.get("/")
def root():
    return "Hello"