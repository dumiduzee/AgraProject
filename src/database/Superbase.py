from supabase import create_client, Client
from decouple import config

superbase :Client = create_client(config("DB_URL"),config("DB_KEY"))

def get_db():
    return superbase