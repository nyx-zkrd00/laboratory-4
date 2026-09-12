import unittest
from unittest.mock import patch
from model import ClinicDatabase, PetOwner, PetFactory, Appointment
import pet_owner_management
import appointment_management

class TestClinicManagementSystem(unittest.TestCase):
    def setUp(self):
        self.db = ClinicDatabase()
        self.db.owners.clear()
        self.db.pets.clear()
        self.db.appointments.clear()

    def test_validate_singleton_instance(self):
        db1 = ClinicDatabase()
        db2 = ClinicDatabase()
        self.assertIs(db1, db2, "ClinicDatabase is not returning a Singleton instance!")

    @patch('builtins.input', side_effect=['O1', 'Nicole', '09999999999'])
    def test_register_pet_owner(self, mock_input):
        pet_owner_management.register_owner()
        self.assertEqual(len(self.db.owners), 1)
        self.assertEqual(self.db.owners[0].owner_id, 'O1')
        self.assertEqual(self.db.owners[0].name, 'Nicole')

    @patch('builtins.input', side_effect=['P1', 'Sophie', '1', 'O1'])
    def test_add_pet_record(self, mock_input):
        self.db.owners.append(PetOwner('O1', 'Nicole', '09999999999'))
        pet_owner_management.add_pet()
        
        self.assertEqual(len(self.db.pets), 1)
        self.assertEqual(self.db.pets[0].pet_id, 'P1')
        self.assertEqual(self.db.pets[0].name, 'Sophie')
        self.assertEqual(self.db.pets[0].pet_type, 'Dog')
        self.assertEqual(self.db.pets[0].owner.owner_id, 'O1')

    def test_schedule_appointment(self):
        owner = PetOwner('O1', 'Nicole', '09999999999')
        pet = PetFactory.create_pet('P1', 'Sophie', 'Dog', owner)
        self.db.pets.append(pet)
        
        appt = appointment_management.schedule('A1', 'P1', '2026-10-15', '14:00')
        
        self.assertIsNotNone(appt)
        self.assertEqual(len(self.db.appointments), 1)
        self.assertEqual(self.db.appointments[0].appointment_id, 'A1')
        self.assertEqual(self.db.appointments[0].status, 'Scheduled')

    def test_cancel_appointment(self):
        owner = PetOwner('O1', 'Nicole', '09999999999')
        pet = PetFactory.create_pet('P1', 'Sophie', 'Dog', owner)
        appt = Appointment('A1', pet, '2026-10-15', '14:00')
        self.db.appointments.append(appt)
        cancelled_appt = appointment_management.cancel_appointment('A1')
        
        self.assertIsNotNone(cancelled_appt)
        self.assertEqual(cancelled_appt.status, 'Cancelled')
        self.assertEqual(self.db.appointments[0].status, 'Cancelled')

if __name__ == '__main__':
    unittest.main()