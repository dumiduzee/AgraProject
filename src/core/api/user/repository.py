from .exceptions import UserRegistrationException,UpdateUserExceptions


def RegisterUserRepository(user,db):
    """
    Register a new user in the system.
    
    Args:
        user (dict): A dictionary containing user details.
    
    Returns:
        dict: A dictionary containing the result of the registration.
    """
    try:
        response = db.table("users").insert(user).execute()
        return response.data
    except Exception as e:
        print(e)
        raise UserRegistrationException("User registration failed due to an unexpected error.")
    


def UpdateUserRepository(user_id,user_data,db):
    try:
        print(user_data)
        
        response = db.table("users").update(user_data).eq("user_id",user_id).execute()
        if response.data:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        raise UpdateUserExceptions()