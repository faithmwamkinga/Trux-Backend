from django.contrib import admin
from .models import CustomOfficer
class CustomOfficerAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email_address','phone_number','custom_id','username','password')
admin.site.register(CustomOfficer,CustomOfficerAdmin)


