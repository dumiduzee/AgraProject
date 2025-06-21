from .repository import RegisterUserRepository,UpdateUserRepository

def RegisterUserService(userData,db):
    """Register a new user with the provided username, email, and password."""
    return RegisterUserRepository(userData, db)


def UpdateUserService(user_id,user_data,db):
    return UpdateUserRepository(user_id,user_data,db)