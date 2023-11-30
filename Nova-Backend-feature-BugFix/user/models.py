from django.contrib.auth.models import AbstractUser,Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, Group,Permission
from django.utils.translation import gettext as _

# from documents.models import PersonalDocument, TruckDocument, CargoDocument


class DriverUser(AbstractUser):
    VERIFICATION_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Verified', 'Verified'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    license_number = models.CharField(max_length=34, unique=True)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField()
    password = models.CharField(max_length=255)
    document_status = models.CharField(max_length=10, choices=VERIFICATION_STATUS_CHOICES, default="Pending")
    verification_status = models.CharField(max_length=10, choices=VERIFICATION_STATUS_CHOICES, default="Pending")
    verification_date = models.DateTimeField(blank=True, null=True)



    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='driver_users',  # Custom related_name
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='driver_users_permissions',  # Custom related_name
        help_text=_('Specific permissions for this user.'),
    )
    
@receiver(post_save, sender=DriverUser)
def update_verification_status(sender, instance, **kwargs):
    if instance.document_status == "Verified" and instance.verification_status == "Pending":
        instance.verification_status = "Verified"
        instance.verification_date = timezone.now()
        instance.save()
    