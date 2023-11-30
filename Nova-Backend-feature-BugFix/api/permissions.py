from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from customOfficers.models import CustomOfficer
from user.models import DriverUser  # Import the models you want to assign permissions to

def create_custom_permissions():
    """
    Create custom permissions for the CustomOfficer and DriverUser models.
    """
    # Get the content types for the models
    custom_officer_content_type = ContentType.objects.get_for_model(CustomOfficer)
    driver_user_content_type = ContentType.objects.get_for_model(DriverUser)

    # Define custom permissions for CustomOfficer
    custom_officer_permissions = [
        Permission.objects.create(
            codename='can_view_custom_officer',
            name='Can view custom officer',
            content_type=custom_officer_content_type,
        ),
        Permission.objects.create(
            codename='can_change_custom_officer',
            name='Can change custom officer',
            content_type=custom_officer_content_type,
        ),
        # Add more custom permissions for CustomOfficer as needed
    ]

    # Define custom permissions for DriverUser
    driver_user_permissions = [
        Permission.objects.create(
            codename='can_view_driver_user',
            name='Can view driver user',
            content_type=driver_user_content_type,
        ),
        Permission.objects.create(
            codename='can_change_driver_user',
            name='Can change driver user',
            content_type=driver_user_content_type,
        ),
        # Add more custom permissions for DriverUser as needed
    ]

    return custom_officer_permissions, driver_user_permissions

def assign_permissions_to_group(group_name, permissions):
    """
    Assign custom permissions to a group.
    """
    try:
        group = Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return

    # Define which permissions to assign to the group
    permissions_to_assign = Q(codename__in=permissions)

    # Assign permissions to the group
    group.permissions.set(Permission.objects.filter(permissions_to_assign))

# Call the functions to create and assign custom permissions when the module is loaded
custom_officer_permissions, driver_user_permissions = create_custom_permissions()
assign_permissions_to_group('CustomOfficerGroup', custom_officer_permissions)
assign_permissions_to_group('DriverUserGroup', driver_user_permissions)
