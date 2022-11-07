from rest_framework import serializers
from .models import *


class DoctorViewSerializer(serializers.ModelSerializer):
    doctor_speciality_name = serializers.CharField(source='doctor_speciality.doctor_speciality_name', read_only=True)

    class Meta:
        model = Doctors
        fields = ['doctor_id', 'doctor_name', 'doctor_surname', 'doctor_patricity', 'doctor_speciality_name']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['doctor_name', 'doctor_surname', 'doctor_patricity', 'doctor_speciality']


class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsAppointment
        fields = '__all__'


class DoctorsSpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSpecialityDirectory
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'


class TempSerializer(serializers.Serializer):
    doctor_id = models.IntegerField(primary_key=True)
    doctor_name = models.CharField(max_length=20)
    doctor_surname = models.CharField(max_length=20)
    doctor_patricity = models.CharField(max_length=20)
    doctor_speciality = models.ForeignKey(DoctorSpecialityDirectory, models.DO_NOTHING, blank=True, null=True)
    doctor_values = DoctorAppointmentSerializer(DoctorsAppointment.objects.all(), many=True)


class AppointmentSerializerToGet(serializers.ModelSerializer):
    # patient = PatientSerializer(Patients.objects.all())
    class Meta:
        model = DoctorsAppointment
        depth = 1
        fields = ['doctor_appointment_id', 'patient', 'health_complaints', 'date_of_admission']

