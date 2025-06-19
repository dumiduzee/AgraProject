from .exceptions import UserRegistrationException


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
    