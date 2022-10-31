import random
from datetime import datetime

import psycopg2 as psycopg2

names_str = 'Григорий, Лев, Андрей, Роман, Арсений, Степан, Владислав, Никита, Глеб, Марк, Давид, Ярослав, Евгений, Матвей, Фёдор, Николай, Алексей, Андрей, Артемий, Виктор, Никита, Даниил, Денис, Егор, Игорь, Лев, Леонид, Павел, Петр, Роман, Руслан, Сергей, Семён, Тимофей'
surname_str = 'Смирнов Иванов Кузнецов Соколов Попов Лебедев Козлов Новиков Морозов Петров Волков Соловьёв Васильев Зайцев Павлов Семёнов Голубев Виноградов Богданов Воробьёв Фёдоров Михайлов Беляев Тарасов Белов'
patricity_str = 'Григорьевич, Львович, Андреевич, Романович, Арсеньевич, Степанович, Владиславович, Никитович, Глебович, Маркович, Давидович, Ярославович, Евгеньевич, Матвеевич, Фёдоровоич'
health_complains_str = 'Болезнь, Проверка, Выписка больничного листа, Ежегодный осмотр'

names_dict = names_str.split(', ')
surname_dict = surname_str.split(' ')
patricity_dict = patricity_str.split(', ')
health_complains_dict = health_complains_str.split(', ')

doctors_json = []
patient_json = []
appointment_json = []

connect = psycopg2.connect(host="94.190.71.245",
                           port="5432",
                           dbname="web_curs_work",
                           user="postgres",
                           password="03354240")
cursor = connect.cursor()


def random_date(start_date, end_date):
    ts_end = end_date.timestamp()
    ts_start = start_date.timestamp()
    return random.randint(int(ts_start), int(ts_end))


def fill_doctors(value):
    for i in range(value):
        names_rand_int = random.randint(0, len(names_dict) - 1)
        surname_rand_int = random.randint(0, len(surname_dict) - 1)
        patricity_rand_int = random.randint(0, len(patricity_dict) - 1)
        rand_speciality = random.randint(1, 5)
        temp_json = {
            'doctor_name': names_dict[names_rand_int],
            'doctor_surname': surname_dict[surname_rand_int],
            'doctor_patricity': patricity_dict[patricity_rand_int],
            'doctor_speciality_id': rand_speciality
        }
        doctors_json.append(temp_json)


def fill_patients(value):
    for i in range(value):
        names_rand_int = random.randint(0, len(names_dict) - 1)
        surname_rand_int = random.randint(0, len(surname_dict) - 1)
        patricity_rand_int = random.randint(0, len(patricity_dict) - 1)
        rand_speciality = random.randint(1, 5)
        temp_json = {
            'patient_name': names_dict[names_rand_int],
            'patient_surname': surname_dict[surname_rand_int],
            'patient_patricity': patricity_dict[patricity_rand_int],
            'patient_ser_passport': random.randint(1000, 9999),
            'patient_numb_passport': random.randint(100000, 999999),
            'patient_medical_policy': random.randint(1000000000000000, 9999999999999999)
        }
        patient_json.append(temp_json)


def fill_appointments(min_doctors, max_doctors, min_patient, max_patient, value):
    for i in range(value):
        doctor_id = random.randint(min_doctors, max_doctors)
        patient_id = random.randint(min_patient, max_patient)
        temp_json = {
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'health_complaints': health_complains_dict[random.randint(0, len(health_complains_dict) - 1)],
            'date_of_admission': str(datetime.fromtimestamp(random_date(datetime(2020, 10, 28, 8, 0, 0), datetime.now())))
        }
        appointment_json.append(temp_json)


def main():
    fill_doctors(10000)
    fill_patients(10000)
    normal_doctors_json = str(doctors_json).replace('\'', '"')
    normal_patients_json = str(patient_json).replace('\'', '"')
    doctors_query = f'INSERT INTO doctors (doctor_name, doctor_surname, doctor_patricity, doctor_speciality_id) ' \
                    f'SELECT doctor_name, doctor_surname, doctor_patricity, doctor_speciality_id' \
                    f' FROM json_populate_recordset (NULL::doctors, \'{normal_doctors_json}\')'
    patients_query = f'INSERT INTO patients (patient_name, patient_surname, patient_patricity, patient_ser_passport,' \
                     f'patient_numb_passport, patient_medical_policy)' \
                     f'SELECT patient_name, patient_surname, patient_patricity, patient_ser_passport,' \
                     f' patient_numb_passport, patient_medical_policy ' \
                     f' FROM json_populate_recordset (NULL::patients, \'{normal_patients_json}\')'

    # cursor.execute(doctors_query)
    appointment_params_query = 'SELECT min(patient_id), max(patient_id), min(doctor_id), max(doctor_id) from patients,' \
                               'doctors'
    cursor.execute(appointment_params_query)
    params = cursor.fetchall()
    fill_appointments(params[0][2], params[0][3], params[0][0], params[0][1], 10000)
    n_appointment_json = str(appointment_json).replace('\'', '"')
    appointment_execute_query = f'INSERT INTO doctors_appointment (patient_id, doctor_id, health_complaints, ' \
                                f'date_of_admission) ' \
                                f'SELECT patient_id, doctor_id, health_complaints, date_of_admission from ' \
                                f'json_populate_recordset(NULL::doctors_appointment, \'{n_appointment_json}\')'
    cursor.execute(appointment_execute_query)
    print(appointment_json[0])
    connect.commit()


if __name__ == "__main__":
    main()
