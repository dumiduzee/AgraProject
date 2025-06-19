#create vaccine repository

def create_vaccine_repository(vaccine_data, db):
    """
    Repository to create a new vaccine record in the database.

    Args:
        vaccine_data (dict): Data for the vaccine to be created.
        db (Client): Database client instance.

    Returns:
        dict: Response containing the ID of the created vaccine.
    """
    # Insert the vaccine data into the database
    response = db.table("vaccine").insert(vaccine_data).execute()
    
    # Return the ID of the created vaccine
    return response


# Get all vaccines for a pet
def get_vaccines_repository(pet_id, db):
    """
    Repository to get all vaccines for a specific pet.

    Args:
        pet_id (str): ID of the pet for which to retrieve vaccines.
        db (Client): Database client instance.

    Returns:
        list: List of vaccines for the specified pet.
    """
    # Query the database for vaccines associated with the given pet ID
    response = db.table("vaccine").select("*").eq("pet_id", pet_id).execute()
    
    if response.data:
        return response.data
    return []