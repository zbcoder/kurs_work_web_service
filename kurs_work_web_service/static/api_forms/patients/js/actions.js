//Uses static/patients/elements_actions.js
//Uses static/patients/create_form.js

function add_patient(action_url){
    hide_element('patient-view-content');
    setTimeout(remove_element, 800, 'patient-view-content');
    setTimeout(create_form, 1000);
    document.getElementById('post-form').method = "POST";
    document.getElementById('post-form').action = action_url;
}


function update_patient(action_url){
    hide_element('patient-view-content');
    setTimeout(remove_element, 800, 'patient-view-content');
    setTimeout(create_form, 1000);
    const formElement = document.getElementById('post-form');
    var tr = get_selected_row_data();
    setTimeout(function(){fill_form(tr.children)}, 1000);
    formElement.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(formElement);
        const json = {
            'patient_name': formData.get('patient_name'),
            'patient_surname': formData.get('patient_surname'),
            'patient_patricity': formData.get('patient_patricity'),
            'patient_ser_passport': formData.get('patient_ser_passport'), 
            'patient_numb_passport': formData.get('patient_numb_passport'),
            'patient_medical_policy': formData.get('patient_medical_policy')
        }
        put_function(action_url+document.getElementById('current_id').value, json);
    })
}