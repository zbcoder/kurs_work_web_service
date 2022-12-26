from rest_framework import serializers
from .models import *
from datetime import datetime
import re


class DoctorViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        depth = 1
        fields = ['doctor_id', 'doctor_name', 'doctor_surname', 'doctor_patricity', 'doctor_speciality']



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['doctor_name', 'doctor_surname', 'doctor_patricity', 'doctor_speciality']

    def validate(self, attrs):
            regex = '[0-9]+'
            letter_regex = '[A-Za-zА-Яа-я]+'
            if re.search(regex, attrs['doctor_name']) or re.search(regex, attrs['doctor_surname']) \
                or re.search(regex, attrs['doctor_patricity']):
                    raise serializers.ValidationError("Поля не могут содержать цифр")
            return attrs   
        

class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsAppointment
        fields = '__all__'
        depth = 1

class DoctorAppointmentPPDSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsAppointment
        fields = '__all__'

    # def validate(self, attrs):
    #     format = "%d-%m-%Y %H:%M"
    #     regex = '[0-9]+'
    #     if datetime.strptime(attrs['date_of_admission'], format) < datetime.strptime(datetime.now().strftime(format), format): 
    #         raise serializers.ValidationError("Дата записи не может быть меньше текущей")
    #     if not re.match(regex, attrs['patient']) and not re.match(regex, attrs['doctors']):
    #         raise serializers.ValidationError("Идентификатор доктора не может быть символьным значением")
    #     return attrs


class DoctorsSpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSpecialityDirectory
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

    def validate(self, attrs):
        regex = '[0-9]+'
        letter_regex = '[A-Za-zА-Яа-я]+'
        if re.search(regex, attrs['patient_name']) or re.search(regex, attrs['patient_patricity']) \
            or re.search(regex, attrs['patient_surname']):
                raise serializers.ValidationError("Поля не могут содержать цифр")
        elif re.search(letter_regex, attrs['patient_ser_passport']) or re.search(letter_regex, attrs['patient_numb_passport'])\
            or re.search(letter_regex, attrs['patient_medical_policy']):
                raise serializers.ValidationError("Поля номера документов не могут содержать буквы")
        return attrs


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



