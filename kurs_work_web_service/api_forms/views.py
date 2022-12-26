from django.shortcuts import render
# Create your views here.
# localhost change on dynamic url
import requests
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect


def doctors(request):
    full_speciality_url = request.scheme + '://' + \
        request.get_host()+'/'+'api_root/doctors/speciality/'
    doctors_url = request.scheme + '://'+request.get_host()+'/'+'api_root/doctors'
    url_mixins = '?'
    for param in request.GET:
        print(request.GET[param])
        url_mixins += param + '='+request.GET[param]+'&'
    if url_mixins == '?':
        url_mixins += 'page=1'
    doctors_speciality = requests.get(full_speciality_url)
    doctors_page = requests.get(doctors_url+url_mixins)
    return render(request, context={'page_content': doctors_page.json(),
                                    'specialities': doctors_speciality.json(),
                                    'user': request.user},
                      template_name='api_forms/doctors_form.html')


def patients(request):
    full_url = request.scheme + '://'+request.get_host()+'/'+'api_root/patients-list/'
    url_mixins = '?'
    for param in request.GET:
        print(request.GET[param])
        url_mixins += param + '='+request.GET[param]+'&'
    if url_mixins == '?':
        url_mixins += 'page=1'
    patient_request = requests.get(full_url+url_mixins)
    return render(request, context={
        'patients': patient_request.json(),
    }, template_name='api_forms/patients.html')


def appointments(request):
    full_url = request.scheme+'://'+request.get_host()+'/'+'api_root/appointments-list'
    url_mixins = '?'
    for param in request.GET:
        print(request.GET[param])
        url_mixins += param + '='+request.GET[param]+'&'
    if url_mixins == '?':
        url_mixins += 'page=1'
    appointments_request = requests.get(full_url+url_mixins)
    return render(request, context={
        'appointments': appointments_request.json(),
    }, template_name='api_forms/appointments_form.html')


def about(request):
    return render(request, template_name='api_forms/about.html')


def auth(request):
    return render(request, template_name='api_forms/auth.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, template_name='registration/registration.html', context={'form': form})
