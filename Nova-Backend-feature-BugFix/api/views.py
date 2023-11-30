from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.backends import ModelBackend
from django.http import JsonResponse
from django.shortcuts import render
from documents.models import Document
from .serializers import (
    DocumentSerializer,
    DocumentVerificationSerializer,
    PersonalDocumentSerializer,
    CargoDocumentSerializer,
    TruckDocumentSerializer,
    CustomOfficerReadSerializer,
    CustomOfficerWriteSerializer,
    DriverReadSerializer,
    DriverWriteSerializer,
)
from rest_framework.decorators import api_view
from customOfficers.models import CustomOfficer
from documents.models import (
    CargoDocument,
    PersonalDocument,
    TruckDocument,
    )
from rest_framework.generics import CreateAPIView
from user.models import DriverUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny




class DriverUserSignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = DriverWriteSerializer(data=request.data)
        if serializer.is_valid():
            # Hash the user's password
            password = serializer.validated_data['password']
            hashed_password = make_password(password)
            serializer.validated_data['password'] = hashed_password

            user = serializer.save()
            response_data = {
                "message": "Signup successful.",
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DriverUserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        print("username:", username)
        print("Password:", password)

        user = authenticate(request, username=username, password=password)
        print("User:", user)
        if user is not None:
           
            print("User authenticated:", user)
            response_data = {
                "message": "Login successful.",
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            
            print("Authentication failed")
            response_data = {
                "message": "Invalid credentials.",
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)


class DriverUserListView(APIView):
    

    def get(self, request):
        drivers = DriverUser.objects.all()
        serializer =  DriverReadSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DriverUserDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            driver = DriverUser.objects.get(id=id)
            serializer = DriverReadSerializer(driver)
            
            # Retrieve all documents associated with the driver
            # cargo_document = driver.cargo_document.all()
            documents = driver.documents.all()
            document_serializer = DocumentSerializer(documents, many=True)
            
            # Include documents in the response data
            response_data = {
                'driver_info': serializer.data,
                'documents': document_serializer.data,
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        except DriverUser.DoesNotExist:
            return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)





class CustomUserSignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = CustomOfficerWriteSerializer(data=request.data)
        if serializer.is_valid():
            # Hash the user's password
            password = serializer.validated_data['password']
            hashed_password = make_password(password)
            serializer.validated_data['password'] = hashed_password

            user = serializer.save()
            response_data = {
                "message": "Signup successful.",
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomUserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        print("username:", username)
        print("Password:", password)

        user = authenticate(request, username=username, password=password)
        print("User:", user)
        if user is not None:
           
            print("User authenticated:", user)
            response_data = {
                "message": "Login successful.",
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            
            print("Authentication failed")
            response_data = {
                "message": "Invalid credentials.",
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)


class CustomOfficerListView(APIView):
    def get(self, request):
        customs = CustomOfficer.objects.all()
        serializer = CustomOfficerReadSerializer(customs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomOfficerReadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomOfficerDetailView(APIView):
    def get_object(self, id):
        try:
            return CustomOfficerReadSerializer.objects.get(id=id)
        except CustomOfficerReadSerializer.DoesNotExist:
            raise NotFound()

    def get(self, request, id, format=None):
        custom = self.get_object(id)
        serializer = CustomOfficerReadSerializer(custom)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        custom = self.get_object(id)
        serializer = CustomOfficerReadSerializer(custom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DocumentListView(APIView):
    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DocumentDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            document = Document.objects.get(id=id)
            serializer = DocumentSerializer(document)
            return Response(serializer.data)
        except Document.DoesNotExist:
            return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, id, format=None):
        try:
            document = Document.objects.get(id=id)
        except Document.DoesNotExist:
            return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentSerializer(document, data=request.data)
    def delete(self, request, id, format=None):
        try:
            document = Document.objects.get(id=id)
        except Document.DoesNotExist:
            return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
        document.delete()
        return Response("Successfully Deleted", status=status.HTTP_204_NO_CONTENT)



            


class PersonalDocumentListView(APIView):
    def get(self, request):
        documents = PersonalDocument.objects.all( )
        serializer = PersonalDocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonalDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

class PersonalDocumentDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            document = PersonalDocument.objects.get(id=id)
            serializer = PersonalDocumentSerializer(document)
            return Response(serializer.data)
        except Document.DoesNotExist:
            return Response({"error": "Personal Document not found"}, status=status.HTTP_404_NOT_FOUND)

            

    def put(self, request, id, format=None):
        try:
            document = PersonalDocument.objects.get(id=id)
        except PersonalDocument.DoesNotExist:
            return Response({"error": "Personal Document not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonalDocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        try:
            document = PersonalDocument.objects.get(id=id, is_personal=True)
        except PersonalDocument.DoesNotExist:
            return Response({"error": "Personal Document not found"}, status=status.HTTP_404_NOT_FOUND)
        document.delete()
        return Response("Successfully Deleted", status=status.HTTP_204_NO_CONTENT)

class TruckDocumentListView(APIView):
    def get(self, request):
        documents = TruckDocument.objects.all()
        serializer = TruckDocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TruckDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TruckDocumentDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            document = TruckDocument.objects.get(id=id)
            serializer = DocumentSerializer(document)
            return Response(serializer.data)
        except Document.DoesNotExist:
            return Response({"error": "Truck Document not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        try:
            document = TruckDocument.objects.get(id=id)
        except TruckDocument.DoesNotExist:
            return Response({"error": "Truck Document not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TruckDocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        try:
            document = TruckDocument.objects.get(id=id, is_personal=False)
        except TruckDocument.DoesNotExist:
            return Response({"error": "Truck Document not found"}, status=status.HTTP_404_NOT_FOUND)
        document.delete()
        return Response("Successfully Deleted", status=status.HTTP_204_NO_CONTENT)

class CargoDocumentListView(APIView):
    def get(self, request):
        cargo = CargoDocument.objects.all()
        serializer = CargoDocumentSerializer(cargo, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CargoDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CargoDocumentDetailView(APIView):

    def get(self, request, id, format=None):
        try:
            cargo_document = CargoDocument.objects.get(id=id)
            serializer = CargoDocumentSerializer(cargo_document)
            return Response(serializer.data)
        except CargoDocument.DoesNotExist:
            return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, id, format=None):
        try:
            cargo_document = CargoDocument.objects.get(id=id)
        except CargoDocument.DoesNotExist:
            return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentSerializer(cargo_document, data=request.data)
    def delete(self, request, id, format=None):
        try:
            cargo_document = CargoDocument.objects.get(id=id)
        except CargoDocument.DoesNotExist:
            return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
        cargo_document.delete()
        return Response("Successfully Deleted", status=status.HTTP_204_NO_CONTENT)


class DocumentVerficationView(APIView):
    permission_classes = []
   
    def post(self, request, document_id):
        try:
            document = Document.objects.get(id=document_id)
        except Document.DoesNotExist:
            return Response({"detail": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if document.is_verified:
            return Response({"detail": "Document already verified"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DocumentVerificationSerializer(data=request.data)
        if serializer.is_valid():

            document.is_verified = True
            document.save()

            return Response({"detail": "Document Verification Successful"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
