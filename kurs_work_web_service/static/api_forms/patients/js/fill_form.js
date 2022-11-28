function fill_form(td_array){
    console.log(td_array.item(5).innerHTML)
    document.getElementById('patient-surname').value = td_array.item(1).innerHTML;
    document.getElementById('patient-name').value =td_array.item(2).innerHTML;
    document.getElementById('patient-patricity').value = td_array.item(3).innerHTML;
    document.getElementById('patient_ser').value = td_array.item(4).innerHTML.split(' ')[0];
    document.getElementById('patient_numb').value = td_array.item(4).innerHTML.split(' ')[1];
    document.getElementById('patient_medical_polycy').value = td_array.item(5).innerHTML;
}