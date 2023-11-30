from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser,Permission,Group
from django.utils.translation import gettext as _

class CustomOfficer(AbstractUser):
    username = models.CharField(max_length=100, default="username")
    first_name = models.CharField(default=True)
    last_name = models.CharField(default=True)
    email_address = models.EmailField(default=True)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=255)
    custom_id = models.CharField(max_length=255, unique=True)
    user_permission=models.ManyToManyField(Permission,related_name="user_custom")

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_users',  
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_users_permissions',  
        help_text=_('Specific permissions for this user.'),
    )
    
    
   