#Create record in pet table

def InsertPet(petData,db):
    response = db.table("pet_table").insert(petData).execute()
    return response.data