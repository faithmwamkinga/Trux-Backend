from rest_framework import serializers , validators
from customOfficers.models import CustomOfficer
from documents.models import (
    PersonalDocument,
    CargoDocument,
    TruckDocument,
    Document
    )

from user.models import DriverUser
from django.contrib.auth.models import User
from rest_framework import serializers





class CustomOfficerReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomOfficer
        fields = ('id', 'username', 'email_address', 'first_name', 'last_name', 'phone_number', 'custom_id')

class CustomOfficerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomOfficer
        fields = ('id', 'username', 'email_address', 'first_name', 'last_name', 'phone_number', 'custom_id', 'password')


class DriverReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone', 'license_number','verification_status')

class DriverWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone', 'license_number','password')      
        
        


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class CargoDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoDocument
        fields = '__all__'       

    


class PersonalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDocument
        fields = '__all__'                        


class TruckDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckDocument
        fields = '__all__'        


class DocumentVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['is_verified']