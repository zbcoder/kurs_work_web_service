from django.urls import path
from .views import *

urlpatterns = [
    path(r'doctors/', doctors),
    path(r'appointments/', appointments),
    path(r'patients/', patients)
]