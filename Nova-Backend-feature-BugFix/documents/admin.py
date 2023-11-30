from django.contrib import admin
from .models import PersonalDocument, TruckDocument, CargoDocument

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_documents=("name","reference_number","issue_date","expiry_date","document_type","document_image","cargo","cargo_tones")

admin.site.register(PersonalDocument, DocumentAdmin)    
admin.site.register(TruckDocument, DocumentAdmin)
admin.site.register(CargoDocument, DocumentAdmin)

