from django.contrib.auth.backends import ModelBackend
from .models import DriverUser

class DriverModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user =  DriverUser.objects.get(username=username)
        except DriverUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        
        return None