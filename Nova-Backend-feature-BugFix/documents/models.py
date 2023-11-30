from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from decimal import Decimal

from user.models import DriverUser



class Document(models.Model):

    driver = models.ForeignKey(DriverUser, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=100, null=True, blank=True, unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    document_image = models.FileField(upload_to='images/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    verification_date = models.DateTimeField(null=True, blank=True, editable=False)
    upload_date = models.DateTimeField(default=timezone.now, editable=False)
    modification_date = models.DateTimeField(null=True, blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        
        if not self.pk:
            self.upload_date = timezone.now()
        
        self.modification_date = timezone.now()
        super().save(*args, **kwargs)
   
    def __str__(self):
        return self.document_type


class PersonalDocument(Document):
    DOCUMENT_TYPES_CHOICES = [
        ('passport', 'Passport'),
        ('driving_license', 'Driving License'),
        ('health_certificate', 'Health Certificate')
    ]

    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES_CHOICES)

    class Meta:
        verbose_name = "Personal Document"
        verbose_name_plural = "Personal Documents"


class TruckDocument(Document):
    DOCUMENT_TYPES_CHOICES = [
        ('insurance', 'Insurance'),
        ('transit goods documents', 'Certified Tansit Goods Document'),
        
    ]

    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES_CHOICES)

    class Meta:
        verbose_name = "Truck Document"
        verbose_name_plural = "Truck Documents"


class CargoDocument(Document):
    DOCUMENT_TYPES_CHOICES = [
        ('t1_document', 'T1 Document'),
        ('c2_document', 'C2 Document'),
        ('cargo_declaration', 'Cargo Declaration')
    ]

    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES_CHOICES)
    cargo = models.CharField(max_length=100)
    cargo_tones = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('00.00'))


    class Meta:
        verbose_name = "Cargo Document"
        verbose_name_plural = "Cargo Documents"


@receiver(post_save, sender=PersonalDocument)
@receiver(post_save, sender=TruckDocument)
@receiver(post_save, sender=CargoDocument)
def update_verification_date(sender, instance, **kwargs):
    if instance.is_verified and not instance.verification_date:
        instance.verification_date = timezone.now()
        instance.save()

    driver = instance.driver

    personal_documents = PersonalDocument.objects.filter(driver=driver)
    truck_documents = TruckDocument.objects.filter(driver=driver)
    cargo_documents = CargoDocument.objects.filter(driver=driver)

    personal_verified = personal_documents.exists() and all(document.is_verified for document in personal_documents)
    truck_verified = truck_documents.exists() and all(document.is_verified for document in truck_documents)
    cargo_verified = cargo_documents.exists() and all(document.is_verified for document in cargo_documents)

    if personal_verified and truck_verified and cargo_verified:
        driver.document_status = 'Verified'
       
    else:
        driver.document_status = 'Pending'
       
    driver.save()
