from django.urls import include, path
from .views import *

urlpatterns = [
    path(r'doctors/', doctors, name='forms-doctors'),
    path(r'appointments/', appointments, name='forms-appointments'),
    path(r'patients/', patients, name='forms-patients'),
    path(r'about/', about, name='forms-about'),
    path(r'', include('django.contrib.auth.urls')),
]