from .repository import createAppointmentRepository,getAppointmentsRepository,updateAppointmentRepository

#Handle create new appoinemnt for pet
def creteAppoinmentService(appoinment, db):
    """
    Handle the creation of a new appointment for a pet.
    
    Args:
        appoinment: The appointment data to be created.
        db: The database client to interact with the database.
    
    Returns:
        The result of the appointment creation operation.
    """
    # Here you would typically insert the appointment into the database
    # For example:
    # result = db.insert("appointments", appoinment.dict())
    # return result
    return createAppointmentRepository(appoinment, db)
# Replace with actual implementation


#Get appoinments to specific pet
def getAppoinmentsService(pet_id, db):
    return getAppointmentsRepository(pet_id, db)


#Update appoinment service
def updateAppoinmentService(appoinment_id, appoinment, db):
    """
    Handle the update of an existing appointment for a pet.
    
    Args:
        appoinment_id: The ID of the appointment to be updated.
        appoinment: The updated appointment data.
        db: The database client to interact with the database.
    
    Returns:
        The result of the appointment update operation.
    """
    # Here you would typically update the appointment in the database
    # For example:
    # result = db.update("appointments", appoinment.dict()).where("id", appoinment_id).execute()
    # return result
    return updateAppointmentRepository(appoinment_id, appoinment, db)

