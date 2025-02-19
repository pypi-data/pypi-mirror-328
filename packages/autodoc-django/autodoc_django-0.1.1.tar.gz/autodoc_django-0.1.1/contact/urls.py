from django.urls import path
from ottoboni.contact import views

urlpatterns = [
    path('obrigado/', views.ContactSuccess.as_view(), name='contact_success'),
    path('', views.Contact.as_view(), name='contact'),
]
