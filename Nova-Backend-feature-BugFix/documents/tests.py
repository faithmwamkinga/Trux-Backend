import datetime
from django.test import TestCase
from documents.models import Document

class DocumentTestCase(TestCase):
    def setUp(self):
        self.document_type = 'Personal'
        self.document_image = 'images/image.jpg'
        self.document = Document.objects.create(
            name='Driving license',
            reference_number='ABC123',
            issue_date=datetime.date(2020, 1, 1),
            expiry_date=datetime.date(2025, 1, 1),
            document_type=self.document_type,
            document_image=self.document_image,
        )

    def test_name_max_length(self):
        max_length = self.document._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_reference_number_null(self):
        field_null = self.document._meta.get_field('reference_number').null
        self.assertTrue(field_null)

    def test_reference_number_blank(self):
        field_blank = self.document._meta.get_field('reference_number').blank
        self.assertTrue(field_blank)

    def test_reference_number_unique(self):
        field_unique = self.document._meta.get_field('reference_number').unique
        self.assertTrue(field_unique)

    def test_issue_date_type(self):
        field_type = self.document._meta.get_field('issue_date').get_internal_type()
        self.assertEqual(field_type, 'DateField')

    def test_expiry_date_type(self):
        field_type = self.document._meta.get_field('expiry_date').get_internal_type()
        self.assertEqual(field_type, 'DateField')

    def test_document_type_choices(self):
        choices = self.document._meta.get_field('document_type').choices
        self.assertEqual(choices, Document.DOCUMENT_TYPES)

    def test_document_image_upload_to(self):
        upload_to = self.document._meta.get_field('document_image').upload_to
        self.assertEqual(upload_to, 'images')