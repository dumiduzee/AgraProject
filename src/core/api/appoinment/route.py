from fastapi import APIRouter,Depends
from .schema import AppointmentSchema,AppointmentResponseSchema,GetAppointmentResponseSchema,AppoinmentUpdateSchema,AppointmentUpdateResponseSchema
from database.Superbase import Client,get_db
from typing import Annotated
from .service import creteAppoinmentService,getAppoinmentsService,updateAppoinmentService

router = APIRouter(tags=["Appoinment"])


@router.get("/{pet_id}",description="Use for get all appoinment for pet",response_model=GetAppointmentResponseSchema)
def getAppoinments(pet_id: str, db: Annotated[Client, Depends(get_db)]):
    response = getAppoinmentsService(pet_id, db)
    return GetAppointmentResponseSchema(
        status=True,
        message="Appointments retrieved successfully",
        appointments=response
    )


# Create a new appointment for pet
@router.post("/create",description="Use for create new appointment for pet",response_model=AppointmentResponseSchema)
def NewAppoinment(appoinment:AppointmentSchema,db:Annotated[Client, Depends(get_db)]):
    response = creteAppoinmentService(appoinment.model_dump(), db)
    return AppointmentResponseSchema(id=response["id"], status=True, message="Appointment created successfully")


#Update appoinment
@router.put("/update/{appoinment_id}", description="Use for update appointment for pet",response_model=AppointmentUpdateResponseSchema)
def updateAppoinment(appoinment_id: str, appoinment: AppoinmentUpdateSchema, db: Annotated[Client, Depends(get_db)]):
    # Here you would typically update the appointment in the database
    # For example:
    # result = db.update("appointments", appoinment.dict()).where("id", appoinment_id).execute()
    # return result
    # print(appoinment_id, appoinment, db)
    response = updateAppoinmentService(appoinment_id, appoinment.model_dump(), db)
    if response:
        return AppointmentUpdateResponseSchema(status=True, message="Appointment updated successfully")
    else:
        return AppointmentUpdateResponseSchema(status=False, message="Failed to update appointment")