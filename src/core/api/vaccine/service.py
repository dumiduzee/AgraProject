from .repository import create_vaccine_repository,get_vaccines_repository

#create vaccine service

def create_vaccine_service(vaccine_data, db):
    """
    Service to create a new vaccine record in the database.

    Args:
        vaccine_data (dict): Data for the vaccine to be created.
        db (Client): Database client instance.

    Returns:
        dict: Response containing the ID of the created vaccine.
    """
    # Insert the vaccine data into the database
    response = create_vaccine_repository(vaccine_data, db)
    if response:
        return response.data
    return None
    # Return the ID of the created vaccine



    #Get all vaccines for a pet
def get_vaccines_service(pet_id, db):
    """
    Service to get all vaccines for a specific pet.

    Args:
        pet_id (str): ID of the pet for which to retrieve vaccines.
        db (Client): Database client instance.

    Returns:
        list: List of vaccines for the specified pet.
    """
    # Query the database for vaccines associated with the given pet ID
    response = get_vaccines_repository(pet_id, db)
    
    if response:
        return response
    return []
    
