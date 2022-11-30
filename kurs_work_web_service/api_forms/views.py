from django.shortcuts import render
# Create your views here.
# localhost change on dynamic url
import requests


def doctors(request):
    if request.method == 'GET':
        print('\n\n\nGET: ', request.GET, '\n\n\n\n')
        try:
            page = request.GET['page']
        except:
            page = 1
        try:
            page_size = request.GET['page_size']
        except:
            page_size=15
        try:
            filter = request.GET['filter']
        except:
            filter = ''
        doctors_speciality = requests.get(f'http://127.0.0.1:8000/api_root/doctors/speciality/')
        doctors_page = requests.get(f'http://127.0.0.1:8000/api_root/doctors?page={str(page)}&page_size={str(page_size)}&filter={str(filter)}')
        print(doctors_page)
        return render(request, context={'page_content': doctors_page.json(),
                                        'specialities': doctors_speciality.json(),
                                        'user': request.user},
                      template_name='api_forms/doctors_form.html')


def appointments(request):

    return render(request, context={}, template_name='api_forms/appointments_form.html')


def patients(request):
    print(request.GET)
    url_mixins = '?'
    for param in request.GET:
        print(request.GET[param])
        url_mixins += param +'='+request.GET[param]+'&'
    if url_mixins == '?':
        url_mixins+='page=1'
    patient_request = requests.get('http://127.0.0.1:8000/api_root/patients-list/'+url_mixins)
    return render(request, context={
        'patients': patient_request.json(),
    }, template_name='api_forms/patients.html')


def appointments(request):
    url_mixins = '?'
    for param in request.GET:
        print(request.GET[param])
        url_mixins += param +'='+request.GET[param]+'&'
    if url_mixins == '?':
        url_mixins+='page=1'
    appointments_request = requests.get('http://127.0.0.1:8000/api_root/appointments-list/'+url_mixins)
    return render(request, context={
        'appointments': appointments_request.json(),
    }, template_name='api_forms/appointments_form.html')


def about(request):
    return render(request, template_name='api_forms/about.html')


def auth(request):
    return render(request, template_name='api_forms/auth.html')
