from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class DoctorsDetail(APIView):
    def get_object(self, pk):
        try:
            return Doctors.objects.get(pk=pk)
        except Doctors.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

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


class DoctorView(APIView):

    def get(self, request, format=None):
        doctors = Doctors.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentView(APIView):

    def get(self, request, format=None):
        appointment = DoctorsAppointment.objects.all()
        print()
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
