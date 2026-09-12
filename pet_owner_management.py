from model import PetOwner, Pet

owners = []
pets = []



def register_owner():
    print("\nREGISTER NEW PET OWNER")

    owner_id = input("Enter Owner ID: ")
    name = input("Enter Owner Name: ")
    contact_number = input("Enter Contact Number: ")

    owner = PetOwner(owner_id, name, contact_number)
    owners.append(owner)

    print("\nPet owner registered successfully!")


def view_owners():
    print("\nREGISTERED PET OWNERS")

    if len(owners) == 0:
        print("No registered pet owners.")
        return

    for owner in owners:
        print(f"Owner ID: {owner.owner_id}")
        print(f"Name: {owner.name}")
        print(f"Contact Number: {owner.contact_number}")



def add_pet():
    print("\nADD PET RECORD")

    if len(owners) == 0:
        print("Please register a pet owner first.")
        return

    pet_id = input("Enter Pet ID: ")
    name = input("Enter Pet Name: ")

    print("\nPet Types:")
    print("1. Dog")
    print("2. Cat")
    print("3. Bird")
    print("4. Rabbit")

    choice = input("Choose pet type: ")

    pet_types = {
        "1": "Dog",
        "2": "Cat",
        "3": "Bird",
        "4": "Rabbit"
    }

    if choice not in pet_types:
        print("Invalid pet type.")
        return

    pet_type = pet_types[choice]

    print("\nREGISTERED OWNERS")

    for owner in owners:
        print(f"{owner.owner_id} - {owner.name}")

    owner_id = input("\nEnter Owner ID: ")

    owner = None

    for registered_owner in owners:
        if registered_owner.owner_id == owner_id:
            owner = registered_owner
            break

    if owner is None:
        print("Owner not found.")
        return

    pet = Pet(pet_id, name, pet_type, owner)
    pets.append(pet)

    print("\nPet record added successfully!")


def view_pets():
    print("\nREGISTERED PETS")

    if len(pets) == 0:
        print("No registered pets.")
        return

    for pet in pets:
        print(f"Pet ID: {pet.pet_id}")
        print(f"Pet Name: {pet.name}")
        print(f"Pet Type: {pet.pet_type}")
        print(f"Owner: {pet.owner.name}")
        print(f"Owner ID: {pet.owner.owner_id}")