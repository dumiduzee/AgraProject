from fastapi import APIRouter


router = APIRouter(tags=["Vaccine"])


@router.get("/")
def root():
    return "Hello"