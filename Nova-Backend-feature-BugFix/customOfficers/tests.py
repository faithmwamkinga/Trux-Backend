from django.test import TestCase
from customOfficers.models import CustomOfficer

class CustomOfficerModelTestCase(TestCase):
    def setUp(self):
        self.custom_officer = CustomOfficer.objects.create(
            first_name='John',
            last_name='Mwangi',
            email_address='mwangijohn@gmail.com',
            located_border='Busia',
            phone_number='0734567890',
            password='mwangi123',
            custom_id='1245123'
        )

    def test_str_representation(self):
        self.assertEqual(str(self.custom_officer), 'John')

    def test_fields(self):
        self.assertEqual(self.custom_officer.first_name, 'John')
        self.assertEqual(self.custom_officer.last_name, 'Mwangi')
        self.assertEqual(self.custom_officer.email_address, 'mwangijohn@gmail.com')
        self.assertEqual(self.custom_officer.located_border, 'Busia')
        self.assertEqual(self.custom_officer.phone_number, '0734567890')
        self.assertEqual(self.custom_officer.password, 'mwangi123')
        self.assertEqual(self.custom_officer.custom_id, '1245123')
        self.assertIsNotNone(self.custom_officer.creation_date)

    def test_null_fields(self):
        custom_officer = CustomOfficer.objects.create(
            first_name='Jane',
            last_name='Maina',
            located_border='Busia',
            phone_number='0776543210',
            password='maina456',
            custom_id='3456456'
        )
       

    def test_unique_custom_id(self):
 
        custom_officer = CustomOfficer(
            first_name='James',
            last_name='Mungai',
            email_address='jamesmwangi@gmail.com',
            located_border='Busia',
            phone_number='0712345678',
            password='james123',
            custom_id='1245123'  
        )
        with self.assertRaises(Exception):
            custom_officer.full_clean()

    def test_blank_located_border(self):
  
        custom_officer = CustomOfficer(
            first_name='James',
            last_name='Mungai',
            email_address='jamesmwangi@gmail.com',
            located_border='',
            phone_number='0711345678',
            password='james123',
            custom_id='9876543'
        )
        with self.assertRaises(Exception):
            custom_officer.full_clean()

    def test_blank_password(self):
  
        custom_officer = CustomOfficer(
            first_name='James',
            last_name='Mungai',
            email_address='jamesmwangi@gmail.com',
            located_border='Busia',
            phone_number='0733345678',
            password='',
            custom_id='9876543'
        )
        with self.assertRaises(Exception):
            custom_officer.full_clean()

    def test_max_length_custom_id(self):
     
        custom_officer = CustomOfficer(
            first_name='James',
            last_name='Mungai',
            email_address='jamesmwangi@gmail.com',
            located_border='Busia',
            phone_number='0744345678',
            password='james123',
            custom_id='1234567' 
        )
        with self.assertRaises(Exception):
            custom_officer.full_clean()

    def test_creation_date_auto_now_add(self):
        initial_creation_date = self.custom_officer.creation_date
        self.custom_officer.save()
        self.assertEqual(initial_creation_date, self.custom_officer.creation_date)