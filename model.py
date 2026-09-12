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


class Appointment:
    def __init__(self, appointment_id, pet, appointment_date, appointment_time):
        self.appointment_id = appointment_id
        self.pet = pet
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.status = "Scheduled"

class ClinicDatabase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClinicDatabase, cls).__new__(cls)
            cls._instance.owners = []
            cls._instance.pets = []
            cls._instance.appointments = []
        return cls._instance

class PetFactory:
    @staticmethod
    def create_pet(pet_id, name, pet_type, owner):
        return Pet(pet_id, name, pet_type, owner)