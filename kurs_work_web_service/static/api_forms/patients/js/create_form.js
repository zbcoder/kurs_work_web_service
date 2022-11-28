//Uses static/js/create_form_elements.js

function create_form(){
    
    new_div_form = document.createElement('div');
    new_div_form.classList.add('fading-content');
    new_div_form.classList.add('fade');
    new_div_form.id ='fading-form'

    header = document.createElement('h3');
    header.classList.add('fs-3');
    header.classList.add('text-start');
    header.classList.add('fading-content');
    header.classList.add('scaling-content');
    header.classList.add('animated');
    header.id = 'animated-header';
    header.innerHTML = 'Patients form' 
    header.style.cssText = `margin-top: 15px;`
    
    patient_surname = create_input_element('patient-surname', 'maximum 20 symbols', 'Input a patient surname', 'surname_row', 'patient_surname');
    patient_name = create_input_element('patient-name', 'maximum 20 symbols', 'Input a patient name', 'name_row', 'patient_name');
    patient_patricity = create_input_element('patient-patricity', 'maximum 20 symbols', 'Input a doctor patricity', 'patricity_row', 'patient_patricity');
    patient_data = create_multy_row(3, ['4 symbols', '6 symbols', '16 symbols'], 'Input documents data', ['patient_ser_passport', 'patient_numb_passport', 'patient_medical_policy'],
    ['patient_ser', 'patient_numb', 'patient_medical_polycy'], ['Passport ser', 'Passport numb', 'Medical policy number'], "number", ["9999", "999999", "9999999999999999"], 
    ["1000", "1", "1"])
    buttons = create_buttons([['submit', ['btn', 'btn-dark']], ['reset', ['btn', 'btn-outline-danger']]])
    new_div_form.appendChild(header);
    new_div_form.appendChild(patient_surname);
    new_div_form.appendChild(patient_name);
    new_div_form.appendChild(patient_patricity);
    new_div_form.appendChild(patient_data);
    new_div_form.appendChild(buttons);

    
    document.querySelector('#post-form').appendChild(new_div_form);
    setTimeout(function(){document.querySelector('#fading-form').classList.remove('fade')}, 1);
    setTimeout(function(){document.querySelector('#animated-header').classList.remove('animated')}, 20);
}

