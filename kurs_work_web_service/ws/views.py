import requests
from django.shortcuts import render

# Create your views here.
url = 'http://127.0.0.1:8000/api_root/'

def temp_show(request):
    result = requests.get(url+'doctors/')
    return render(request, 'ws/appointment_form.html', {'doctor_list': result.json(), 'range': range(3)})