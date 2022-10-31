from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

urlpatterns = [
    # path(r'doctors/', DoctorsViewSet.as_view()),
    path('doctors/', DoctorsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path(r'doctors/<int:pk>', DoctorsDetail.as_view()),
    path(r'appointments/', AppointmentView.as_view()),
    path(r'appointments/<int:pk>', AppointmentDetailView.as_view()),
    path(r'appointments_by_doctor/<int:doctor>', AppointmentById.as_view()),
    path(r'doctors/speciality/', DoctorsSpecialityView.as_view()),
    path(r'patients/', PatientsView.as_view()),
    path(r'patients/<int:pk>', PatientDetailView.as_view()),
    path(r'temp/<int:pk>', TempClass.as_view()),
]