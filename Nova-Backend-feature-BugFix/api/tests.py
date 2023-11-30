from django.test import TestCase
# from customOfficers.models import CustomOfficer
from cargo_documents.models import CargoDocument
from documents.models import Document
# from verification.models import VerifiedDocument
# from driver.models import Driver
from rest_framework import serializers
from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
# from .models import Document, CustomOfficer, Driver, CargoDocument, VerifiedDocument


class CustomOfficerSerializerTest(TestCase):
    def test_custom_officer_serializer(self):
        officer_data = {
            'username': 'johnsmith',
            'email': 'john@example.com',
            'first_name': 'John',
            'last_name': 'Smith',
            'password': 'password123'
        }
       

class CargoDocumentSerializerTest(TestCase):
    def test_cargo_document_serializer(self):
        document_data = {
            'name': 'Cargo Document',
            'issue_date': datetime.now(),
            'expiry_date': datetime.now(),
            'document_type': 'Type A',
        }
        

class DocumentSerializerTest(TestCase):
    def test_document_serializer(self):
        document_data = {
            'reference_number': '1234',
            'issue_date': datetime.now(),
            'expiry_date': datetime.now(),
            'document_type': 'Type A',
            'document_image': 'image.png'
        }
        

class DriverSerializerTest(TestCase):
    def test_driver_serializer(self):
        driver_data = {
            'username': 'johndoe',
            'email': 'john@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'license_number': 'ABC123',
            'password': 'password123'
        }
        

class VerifiedSerializerTest(TestCase):
    def test_verified_serializer(self):
        verified_data = {
            'document_type': 'Type A',
            'document_type_display': 'Type A Display',
            'verification_status': 'Verified'
        }




class DocumentTests(APITestCase):
    def setUp(self):
        self.document_data = {
            "name": "yellow fever",
            "issue_date": "2020-01-09",
            "expiry_date": "2025-01-25",
            "document_type": "Personal",
        }
        self.document = Document.objects.create(**self.document_data)
        self.url = reverse("document_detail_view", args=[self.document.id])

    def test_list_documents(self):
        url = reverse("document_list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, f"Expected status code {status.HTTP_200_OK}, but received {response.status_code}. Response content: {response.content}")

    def test_create_document(self):
        url = reverse("document_list_view")
        response = self.client.post(url, self.document_data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, f"Expected status code {status.HTTP_201_CREATED}, but received {response.status_code}. Response content: {response.content}")
        self.assertEqual(Document.objects.count(), 2) 
        

    def test_retrieve_document(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, f"Expected status code {status.HTTP_200_OK}, but received {response.status_code}. Response content: {response.content}")
        

    def test_delete_document(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, f"Expected status code {status.HTTP_204_NO_CONTENT}, but received {response.status_code}. Response content: {response.content}")
        self.assertFalse(Document.objects.filter(id=self.document.id).exists())



class CargoDocumentListViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_cargo_documents(self):
        url = reverse('CargoDocumentListView')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_cargo_document(self):
        url = reverse('CargoDocumentListView')
        payload = {
        }
        response = self.client.post(url, data=payload)

class CargoDocumentDetailViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_cargo_document(self):
        cargo_document = CargoDocument.objects.create()
        url = reverse('CargoDocumentDetailView', args=[cargo_document.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

   
    def test_delete_cargo_document(self):
        cargo_document = CargoDocument.objects.create()
        url = reverse('CargoDocumentDetailView', args=[cargo_document.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_invalid_cargo_document(self):
        invalid_id = 9999 
        url = reverse('CargoDocumentDetailView', args=[invalid_id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    
class DocumentTests(APITestCase):
    def setUp(self):
        self.document_data = {
            "name": "yellow fever",
            "issue_date": "2020-01-09",
            "expiry_date": "2025-01-25",
            "document_type": "Personal",
        }
        self.document = Document.objects.create(**self.document_data)
        self.url = reverse("document_detail_view", args=[self.document.id])

    def test_list_documents(self):
        url = reverse("document_list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, f"Expected status code {status.HTTP_200_OK}, but received {response.status_code}. Response content: {response.content}")

    def test_create_document(self):
        url = reverse("document_list_view")
        response = self.client.post(url, self.document_data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, f"Expected status code {status.HTTP_201_CREATED}, but received {response.status_code}. Response content: {response.content}")
        self.assertEqual(Document.objects.count(), 2) 
        

    def test_retrieve_document(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, f"Expected status code {status.HTTP_200_OK}, but received {response.status_code}. Response content: {response.content}")
        

    def test_delete_document(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, f"Expected status code {status.HTTP_204_NO_CONTENT}, but received {response.status_code}. Response content: {response.content}")
        self.assertFalse(Document.objects.filter(id=self.document.id).exists())        

        