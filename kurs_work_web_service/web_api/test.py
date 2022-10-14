import requests
data={'doctor_name': 'Петр'}
params = {'doctor_name': 'Клим',
          'doctor_surname': 'Петров',
          'doctor_patricity': 'Викторович',
          'doctor_speciality': 5}
res = requests.put('http://127.0.0.1:8000/api_root/doctors/1', params)
print(res.status_code)
print(res.content)
res = requests.get('http://127.0.0.1:8000/api_root/doctors/1')
print(res.text)

url = 'http:127.0.0.1/api_root/'

