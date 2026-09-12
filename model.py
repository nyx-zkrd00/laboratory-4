class PetOwner:
    def __init__(self, owner_id, name, contact_number):
        self.owner_id = owner_id
        self.name = name
        self.contact_number = contact_number


class Pet:
    def __init__(self, pet_id, name, pet_type, owner):
        self.pet_id = pet_id
        self.name = name
        self.pet_type = pet_type
        self.owner = owner