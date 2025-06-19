#create appoinment repository
def createAppointmentRepository(appoinment, db):
    """
    Handle the creation of a new appointment for a pet in the database.
    
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
    response = db.table("appointments").insert(appoinment).execute()
    return response.data[0]  # Replace with actual implementation
    pass  # Replace with actual implementation


#for get all the appoinments of specific pet
def getAppointmentsRepository(pet_id, db):
    """
    Retrieve all appointments for a specific pet from the database.
    
    Args:
        pet_id: The ID of the pet for which to retrieve appointments.
        db: The database client to interact with the database.
    
    Returns:
        A list of appointments for the specified pet.
    """
    response = db.table("appointments").select("*").eq("pet_id", pet_id).execute()
    return response.data  # Replace with actual implementation


#Update appoinment repository
def updateAppointmentRepository(appoinment_id, appoinment, db):
    """
    Handle the update of an existing appointment for a pet in the database.
    
    Args:
        appoinment_id: The ID of the appointment to be updated.
        appoinment: The updated appointment data.
        db: The database client to interact with the database.
    
    Returns:
        The result of the appointment update operation.
    """
    response = db.table("appointments").update(appoinment).eq("id", appoinment_id).execute()
    return response.data  # Replace with actual implementation