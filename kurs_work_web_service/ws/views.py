import requests
from django.http import HttpResponse
from django.shortcuts import render
from .create_pagination_flags import *

# Create your views here.
# url = 'http://192.168.31.196:8000/api_root/'
url = 'http://127.0.0.1:8000/api_root/'


def show_doctor_list(request):
    try:
        get_params = request.GET['page']
        result = requests.get(url + 'doctors/?page=' + get_params)
    except:
        result = requests.get(url + 'doctors/')
    result_dict = result.json()
    try:
        _has_next = has_next(result_dict['next'])
        _has_prev = has_prev(result.json()['previous'])
    except:
        return render(request, 'ws/doctors.html', {'doctor_list': result.json(), 'range': range(3)})
    return render(request, 'ws/doctors.html', {'doctor_list': result.json(), 'range': range(3), 'has_prev': _has_prev,
                                               'has_next': _has_next})


def show_doctor_detail(request, doctor_pk):
    doctor = str(doctor_pk)
    result = requests.get(url + 'doctors/' + doctor)
    appointments = requests.get(url + 'appointments_by_doctor/' + doctor)
    doctor_speciality = requests.get(url + 'doctors/speciality/')
    print(result.json())
    return render(request, 'ws/doctor_detail.html', {'doctor_detail': result.json(),
                                                     'doctor_speciality': doctor_speciality.json()})


def create_appointment(request):
    return render(request, 'ws/create_appointment.html', context={})


def show_main_page(request):
    doctors_speciality = requests.get(url+'doctors/speciality/')
    doctors_count = requests.get(url+'get_doctors_count/')
    return render(request, 'ws/main_page.html', context={
        'doctor_speciality': doctors_speciality.json(),
        'doctor_counts': doctors_count.json(),
    })
