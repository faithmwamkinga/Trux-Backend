from django.contrib.auth.backends import ModelBackend
from .models import CustomOfficer

class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user =  CustomOfficer.objects.get(username=username)
        except CustomOfficer.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        
        return None