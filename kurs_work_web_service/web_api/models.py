from django.db import models

# Create your models here.


class DoctorSpecialityDirectory(models.Model):
    doctor_speciality_id = models.IntegerField(primary_key=True)
    doctor_speciality_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'doctor_speciality_directory'


class Doctors(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    doctor_name = models.CharField(max_length=20)
    doctor_surname = models.CharField(max_length=20)
    doctor_patricity = models.CharField(max_length=20)
    doctor_speciality = models.ForeignKey(DoctorSpecialityDirectory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctors'


class DoctorsAppointment(models.Model):
    doctor_appointment_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey('Patients', models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(Doctors, models.DO_NOTHING)
    health_complaints = models.CharField(max_length=255, blank=True, null=True)
    date_of_admission = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'doctors_appointment'


class Patients(models.Model):
    patient_id = models.BigIntegerField(primary_key=True)
    patient_name = models.CharField(max_length=20)
    patient_patricity = models.CharField(max_length=20)
    patient_surname = models.CharField(max_length=20)
    patient_ser_passport = models.CharField(max_length=4, blank=True, null=True)
    patient_numb_passport = models.CharField(max_length=8, blank=True, null=True)
    patient_medical_policy = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patients'