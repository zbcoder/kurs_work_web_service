import requests

res = requests.get('http://127.0.0.1:8000/api_root/doctors/1')
print(res.text)
params = {'doctor_id': 6,
          'doctor_name': 'Григорий',
          'doctor_surname': 'Смирнов',
          'doctor_patricity': 'Александрович',
          'doctor_speciality': 2}
res = requests.put('http://127.0.0.1:8000/api_root/doctors/6', params)
print(res.status_code)
print(res.content)
res = requests.get('http://127.0.0.1:8000/api_root/doctors/1')
print(res.text)


del_res = requests.delete('http://127.0.0.1:8000/api_root/doctors/1')
print(del_res.status_code)