import requests
from django.shortcuts import render

# Create your views here.
url = 'http://127.0.0.1:8000/api_root/'


def show_doctor_list(request):
    result = requests.get(url + 'doctors/')
    return render(request, 'ws/doctors.html', {'doctor_list': result.json(), 'range': range(3)})


def show_doctor_detail(request, doctor_pk):
    doctor = str(doctor_pk)
    result = requests.get(url+'doctors/'+doctor)
    return render(request, 'ws/doctor_detail.html', {'doctor_detail': result.json()})