from django.urls import path
from .views import (
    DriverUserSignupView,
    DriverUserLoginView,
    DriverUserListView,
    DriverUserDetailView,
    CustomOfficerListView,
    CustomOfficerDetailView,
    CargoDocumentListView,
    CargoDocumentDetailView,
    DocumentListView,
    DocumentDetailView,
   
    PersonalDocumentListView,
    PersonalDocumentDetailView,
    TruckDocumentListView,
    TruckDocumentDetailView,
    CustomUserSignupView,
    CustomUserLoginView,
    TruckDocumentListView,
    TruckDocumentDetailView,

    DocumentVerficationView


)
from . import views


urlpatterns = [
    path('driver/signup/', DriverUserSignupView.as_view(), name='driver-signup'),
    path('driver/login/', DriverUserLoginView.as_view(), name='driver-login'),
    path('driverlist/', DriverUserListView.as_view(), name='driver-list'),
    path('driver/<int:id>/', DriverUserDetailView.as_view(), name='driver-detail'),

    # URLs for CustomOfficer views
    path('custom/signup/', CustomUserSignupView.as_view(), name='driver-signup'),
    path('custom/login/', CustomUserLoginView.as_view(), name='driver-login'),
    path('custom/list/', CustomOfficerListView.as_view(), name='custom-list'),
    path('custom/<int:id>/', CustomOfficerDetailView.as_view(), name='custom-detail'),
    
    path("cargo_document/", CargoDocumentListView.as_view(), name="CargoDocumentListView"),
    path("cargo_document/<int:id>/", CargoDocumentDetailView.as_view(), name="CargoDocumentDetailView"),

    path("documents/", DocumentListView.as_view(), name="document-list"),
    path("documents/<int:id>/", DocumentDetailView.as_view(), name="document-detail"),

 

    path('personal-documents/', PersonalDocumentListView.as_view(), name='personal-document-list'),
    path('personal-documents/<int:id>/', PersonalDocumentDetailView.as_view(), name='personal-document-detail'),

    path('truck-documents/', TruckDocumentListView.as_view(), name='personal-document-list'),
    path('truck-documents/<int:id>/', TruckDocumentDetailView.as_view(), name='personal-document-detail'),

    # path('update_verification_status/<int:driver_id>/<int:document_id/', views.update_verification_status, name='update_verification_status'),
    path('documents/<int:document_id>/verify/', DocumentVerficationView.as_view(), name='verify-document')
]