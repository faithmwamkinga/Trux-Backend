from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DriverUser

class DriverUserAdmin(admin.ModelAdmin):
    list_users = ("first_name","last_name", "license_number","email","phone", "password","username")

    

admin.site.register(DriverUser, DriverUserAdmin)
 
