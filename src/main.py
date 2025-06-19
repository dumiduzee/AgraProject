from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from core.api.appoinment.route import router as AppoinmentRouter
from core.api.pet.route import router as PetRouter
from core.api.pills.route import router as PillsRouter
from core.api.vaccine.route import router as VaccineRouter
from core.api.user.route import router as UserRouter

from core.api.pet.exceptions import PetExceptions



app = FastAPI(
    title="PAWfinity - Pet Caring System API",
    description="""
    Welcome to the PAWfinity API documentation!

    This API provides endpoints for managing pet care, including:
    - User registration and authentication
    - Pet registration and profile management
    - Scheduling appointments (e.g., vet visits, grooming)
    - Tracking pet health and vaccination records
    - And much more!

    Our goal is to make pet care seamless and stress-free for pet owners.
    """
)


app.include_router(prefix="/api/v1/user",router=UserRouter)
app.include_router(prefix="/api/v1/pet",router=PetRouter)
app.include_router(prefix="/api/v1/appoinment",router=AppoinmentRouter)
app.include_router(prefix="/api/v1/user/pills",router=PillsRouter)
app.include_router(prefix="/api/v1/user/vaccine",router=VaccineRouter)



#Exception handler for pet related errors
@app.exception_handler(PetExceptions)
async def PetExceptionHandler(request:Request, exc:PetExceptions):
    return JSONResponse(status_code=exc.status_code,content={
        "message":exc.detail,
        "solution":exc.solution
    })