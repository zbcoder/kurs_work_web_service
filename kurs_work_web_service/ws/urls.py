from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path(r'doctors/', show_doctor_list),
    path(r'doctors/<int:doctor_pk>/', show_doctor_detail),
    path(r'appointments/create/', create_appointment),
    path(r'main/', show_main_page),
    path(r'test/', test_html)
]