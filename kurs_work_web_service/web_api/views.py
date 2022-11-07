from django.core.paginator import Paginator
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status, settings, pagination
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from django.conf import settings
from .models import *
from .serializers import *


class ExamplePagination(pagination.PageNumberPagination):
    page_size = 2


class DoctorsDetail(APIView):
    def get_object(self, pk):
        try:
            return Doctors.objects.get(pk=pk)
        except Doctors.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorViewSerializer(doctor)
        serializer_data = serializer.data
        appointments = DoctorsAppointment.objects.select_related('patient').filter(doctor=pk)
        appointments_serializer = AppointmentSerializerToGet(appointments, many=True)
        serializer_data.update({'appointments': appointments_serializer.data})
        return Response(serializer_data)

    def put(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        doctor = self.get_object(pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorsViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorViewSerializer
    # pagination_class = ExamplePagination
    queryset = Doctors.objects.all()


class DoctorView(APIView):
    def get(self, request, format=None):
        doctors = Doctors.objects.all()
        page = self.paginate_queryset(doctors)
        if page is not None:
            serializer = DoctorViewSerializer(doctors, many=True)
            return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentView(APIView):
    def get(self, request, format=None):
        appointment = DoctorsAppointment.objects.all()
        print(appointment.query)
        serializer = DoctorAppointmentSerializer(appointment, many=True)
        return Response({'appointments': serializer.data})

    def post(self, request, format=None):
        serializer = DoctorAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDetailView(APIView):
    def get_object(self, pk):
        try:
            return DoctorsAppointment.objects.get(pk=pk)
        except DoctorsAppointment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = DoctorAppointmentSerializer(appointment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = DoctorAppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        appointment = self.get_object(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentById(APIView):
    def get(self, request, doctor):
        appointment_by_doctor_id = DoctorsAppointment.objects.filter(doctor=doctor)
        print(appointment_by_doctor_id.query)
        serializer = DoctorAppointmentSerializer(appointment_by_doctor_id, many=True)
        return Response(serializer.data)


class DoctorsSpecialityView(APIView):
    def get(self, request):
        queryset = DoctorSpecialityDirectory.objects.all()
        serializer = DoctorsSpecialitySerializer(queryset, many=True)
        return Response(serializer.data)


class PatientsView(APIView):
    def get(self, request):
        patiens_qs = Patients.objects.all()
        serializer = PatientSerializer(patiens_qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetailView(APIView):
    def get_object(self, pk):
        try:
            return Patients.objects.get(pk=pk)
        except Patients.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        patient = self.get_object(pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TempClass(APIView):
    def get(self, request, pk):
        qs = Doctors.objects.get(doctor_id=pk)
        serializer = TempSerializer(qs)
        return Response(serializer.data)


@api_view(['GET'])
def get_count_doctor_speciality(request):
    qs = Doctors.objects.all().select_related('doctor_speciality'). \
        values('doctor_speciality__doctor_speciality_name'). \
        annotate(dbcount=Count('doctor_speciality'))
    dict = [entry for entry in qs]
    print(dict)
    return Response({'data': dict})
