from django.contrib import admin
from django.urls import path
from rest_framework import routers

from .views import *

urlpatterns = [
    path(r'doctors/', DoctorView.as_view()),
    path(r'doctors/<int:pk>', DoctorsDetail.as_view()),
    path(r'appointments/', AppointmentView.as_view()),
    path(r'appointments/<int:pk>', AppointmentDetailView.as_view())
]