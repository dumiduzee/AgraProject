from fastapi import APIRouter


router = APIRouter(tags=["Users"])


@router.get("/")
def root():
    return "Hello"