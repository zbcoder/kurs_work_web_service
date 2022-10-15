from rest_framework import serializers
from .models import *


class DoctorSerializer(serializers.ModelSerializer):
    doctor_speciality_name = serializers.CharField(source='doctor_speciality.doctor_speciality_name', read_only=True)
    class Meta:
        model = Doctors
        fields = ['doctor_id', 'doctor_name', 'doctor_surname', 'doctor_patricity', 'doctor_speciality_name']


class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsAppointment
        fields = '__all__'
