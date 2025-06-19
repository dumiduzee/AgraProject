from .repository import create_pill_repository,get_pills_repository

#create pill service
def create_pill_service(pill, db):
    """
    Handle the creation of a new pill for a pet.
    
    Args:
        pill: The pill data to be created.
        db: The database client to interact with the database.
    
    Returns:
        The result of the pill creation operation.
    """
    # Here you would typically insert the pill into the database
    # For example:
    # result = db.insert("pills", pill.dict())
    # return result
    return create_pill_repository(pill, db)
    

#Get all pills for a pet
def get_pills_service(pet_id, db):
    """
    Retrieve all pills for a specific pet.
    
    Args:
        pet_id: The ID of the pet for which to retrieve pills.
        db: The database client to interact with the database.
    
    Returns:
        A list of pills associated with the specified pet.
    """
    response =  get_pills_repository(pet_id, db)
    if response:
        return response
    return []