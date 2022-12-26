from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

urlpatterns = [
    # path(r'doctors/', DoctorsViewSet.as_view()),
    path(r'doctors/', DoctorsViewSet.as_view({'get': 'list', 'post': 'create'}), name='doctors-api'),
    path(r'doctors/<int:pk>', DoctorsDetail.as_view()),
    path(r'appointments/', AppointmentView.as_view()),
    path(r'appointments/<int:pk>', AppointmentDetailView.as_view()),
    path(r'appointments_by_doctor/<int:doctor>', AppointmentById.as_view()),
    path(r'doctors/speciality/', DoctorsSpecialityView.as_view()),
    path(r'temp/<int:pk>', TempClass.as_view()),
    path(r'get_doctors_count/', get_count_doctor_speciality),
    path(r'patients-list/', ListPatients.as_view(), name='patients-list'),        #CreateListAPIView get post with pagination
    path(r'patients-list/<int:pk>/', ListViewPatient.as_view()),    #RetrieveUpdateDestroyAPIView get/put/delete requests
    path(r'appointments-list/', ListAppointments.as_view(), name='appointment_list'),
    path(r'appointments-list/post', CreateAppointments.as_view(), name='post_appointment'),
    path(r'appointments-list/<int:pk>', ListViewAppointments.as_view())
]