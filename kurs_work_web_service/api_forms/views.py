from django.shortcuts import render

# Create your views here.
import requests


def doctors(request):
    if request.method == 'GET':
        try:
            page = request.GET['page']
        except:
            page = 1
        doctors_page = requests.get(f'http://127.0.0.1:8000/api_root/doctors?page={str(page)}')
        return render(request, context={'page_content': doctors_page.json()},
                      template_name='api_forms/doctors_form.html')
    if request.method == 'POST':
        print()

    if request.method == 'PUT':
        print()

    if request.method == 'DELETE':
        print()

