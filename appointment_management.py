from model import Appointment, ClinicDatabase

db = ClinicDatabase()
VALID_STATUSES = {"Scheduled", "Completed", "Cancelled"}

def find_appointment(appointment_id):
    for appointment in db.appointments:
        if appointment.appointment_id == appointment_id:
            return appointment
    return None

def schedule(appointment_id, pet_id, appointment_date, appointment_time):
    if find_appointment(appointment_id) is not None:
        print("Appointment ID already exists. Please enter a different ID.")
        return None

    pet = None
    for registered_pet in db.pets:
        if registered_pet.pet_id == pet_id:
            pet = registered_pet
            break
    if pet is None:
        print("Pet not found. Please enter a registered Pet ID.")
        return None

    for appointment in db.appointments:
        same_slot = (
            appointment.pet.pet_id == pet_id
            and appointment.appointment_date == appointment_date
            and appointment.appointment_time == appointment_time
            and appointment.status != "Cancelled"
        )
        if same_slot:
            print("This pet already has an appointment at that time.")
            return None

    appointment = Appointment(appointment_id, pet, appointment_date, appointment_time)
    db.appointments.append(appointment)
    return appointment


def cancel_appointment(appointment_id):
    appointment = find_appointment(appointment_id)
    if appointment is None:
        print("Appointment not found. Please enter a valid Appointment ID.")
        return None
    appointment.status = "Cancelled"
    return appointment

def update_appointment_status(appointment_id, status):
    if status not in VALID_STATUSES:
        print("Invalid status. Please choose Scheduled, Completed, or Cancelled.")
        return None

    appointment = find_appointment(appointment_id)
    if appointment is None:
        print("Appointment not found. Please enter a valid Appointment ID.")
        return None
    appointment.status = status
    return appointment

def view_appointments():
    print("\n")
    print("APPOINTMENT SCHEDULE")

    if len(db.appointments) == 0:
        print("No appointments scheduled.")
        return

    for appointment in db.appointments:
        print(f"Appointment ID: {appointment.appointment_id}")
        print(f"Pet: {appointment.pet.name} ({appointment.pet.pet_id})")
        print(f"Date: {appointment.appointment_date}")
        print(f"Time: {appointment.appointment_time}")
        print(f"Status: {appointment.status}")


def schedule_appointment():
    print("\n")
    print("SCHEDULE APPOINTMENT")

    if len(db.pets) == 0:
        print("Please add a pet record first.")
        return

    print("REGISTERED PETS")
    for pet in db.pets:
        print(f"{pet.pet_id} - {pet.name}")

    appointment_id = input("Enter Appointment ID: ")
    pet_id = input("Enter Pet ID: ")
    appointment_date = input("Enter Appointment Date: ")
    appointment_time = input("Enter Appointment Time: ")

    if schedule(appointment_id, pet_id, appointment_date, appointment_time) is not None:
        print("\n")
        print("Appointment scheduled successfully!")


def cancel_scheduled_appointment():
    print("\n")
    print("CANCEL APPOINTMENT")
    appointment_id = input("Enter Appointment ID: ")

    if cancel_appointment(appointment_id) is not None:
        print("\n")
        print("Appointment cancelled successfully!")

def change_appointment_status():
    print("\n")
    print("UPDATE APPOINTMENT STATUS")
    appointment_id = input("Enter Appointment ID: ")

    print("1. Scheduled")
    print("2. Completed")
    print("3. Cancelled")

    status_choices = {"1": "Scheduled", "2": "Completed", "3": "Cancelled"}

    choice = input("Choose status: ")

    if choice not in status_choices:
        print("Invalid status. Please choose 1, 2, or 3.")
        return

    status = status_choices[choice]

    if update_appointment_status(appointment_id, status) is not None:
        print("\n")
        print("Appointment status updated successfully!")