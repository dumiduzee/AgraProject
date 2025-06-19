from fastapi import APIRouter


router = APIRouter(tags=["Pills"])


@router.get("/")
def root():
    return "Hello"