from .exceptions import DeletePetException,PetInsertException

#Create record in pet table
def InsertPet(petData,db):
    try:
        response = db.table("pet_table").insert(petData).execute()
        return response.data
    except Exception as e:
        raise PetInsertException(status_code=500, detail="Internal server error")

# Delete a pet from the system using its ID.
def DeletePet(pet_id, db):
    """
    Delete a pet from the system using its ID.
    
    Args:
        pet_id (str): The ID of the pet to be deleted.
        db (Client): The database client dependency.
    
    Returns:
        None: If the deletion is successful, returns no content.
    """
    
    # Attempt to delete the pet from the database
    response = db.table("pet_table").delete().eq("id", pet_id).execute()
    if response.data is None or len(response.data) == 0:
        raise DeletePetException(status_code=404, detail="Pet not found")

    return response.data


#get all pets of an owner by owner ID.
def GetPet(owner_id, db):
    """
    Get all pets of an owner by owner ID.
    
    Args:
        owner_id (str): The ID of the owner whose pets are to be retrieved.
        db (Client): The database client dependency.
    
    Returns:
        List[Pet]: A list of pets owned by the specified owner.
    """
    response = db.table("pet_table").select("*").eq("owner_id", owner_id).execute()
    return response.data


