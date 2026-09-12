from pet_owner_management import (
    register_owner,
    view_owners,
    add_pet,
    view_pets
)

while True:
    print("\n")
    print("PET CLINIC MANAGEMENT SYSTEM")
    print("1. Register Pet Owner")
    print("2. View Registered Pet Owners")
    print("3. Add Pet Record")
    print("4. View Pet Information")
    print("5. Exit")

    choice = input("\nSelect an option: ")

    if choice == "1":
        register_owner()
    elif choice == "2":
        view_owners()
    elif choice == "3":
        add_pet()
    elif choice == "4":
        view_pets()
    elif choice == "5":
        print("\nThank you!")
        break
    else:
        print("\nInvalid. Please try again.")