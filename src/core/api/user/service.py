from .repository import RegisterUserRepository

def RegisterUserService(userData,db):
    """Register a new user with the provided username, email, and password."""
    return RegisterUserRepository(userData, db)