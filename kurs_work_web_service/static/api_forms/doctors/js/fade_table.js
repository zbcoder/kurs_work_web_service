var specialities;
function set_data(data){
    specialities = data
}

function fade_table(action){
    console.log(action)
    if(action=='upd'){
        var parameters = get_selected_row_data();
        console.log(parameters.children)
        document.getElementById('create_button').innerHTML='Update'
    }
    tb = document.getElementById('doctor_table').rows

    document.getElementById('doctor_table').style.animationName='myAnimation';
    document.getElementById('doctor_table').style.animationDuration='850ms';
    document.getElementById('doctor_table').style.animationFillMode='forwards';

    document.getElementById('pagination-buttons').style.animationName='myAnimation';
    document.getElementById('pagination-buttons').style.animationDuration='850ms';
    document.getElementById('pagination-buttons').style.animationFillMode='forwards';

    document.getElementById('upd_button').style.animationName='myAnimation';
    document.getElementById('upd_button').style.animationDuration='850ms';
    document.getElementById('upd_button').style.animationFillMode='forwards';

    document.getElementById('del_button').style.animationName='myAnimation';
    document.getElementById('del_button').style.animationDuration='850ms';
    document.getElementById('del_button').style.animationFillMode='forwards';

    document.getElementById('pagination-buttons').remove;
    for(i = tb.length-1; i >= 0; i--){
        tb.item(i).style.animationName = 'myAnimation';
        tb.item(i).style.animationDuration = '300ms';
        tb.item(i).style.animationFillMode='forwards'
    }
    setTimeout(remove_table, 900)
    switch(action){
        case 'add':{
            setTimeout(function(){show_create_form(action)}, 1000)
            return;
        }
        case 'upd':{
            setTimeout(function(){show_create_form(action)}, 1000);
            setTimeout(function(){fill_doctor_form(parameters.children)}, 1000);
            return;
        }
    }
    
    
}

function remove_table(){
    console.log('событие обработано');
    document.getElementById('create_button').classList.add('disabled');
    document.getElementById('doctor_table').removeEventListener("onanimationend", remove_table);
    document.getElementById('pagination-buttons').remove();
    document.getElementById('doctor_table').remove();
}

function add_animation(element_id){
    element_id.style.animationName="myAnimation";
    element_id.style=animationDuration="2000ms";
    element_id.style=animationFillMode="forwards";
}

function show_create_form(action){
    var header = document.createElement('h4')
    header.id = 'doctor_header'
    header.innerHTML = 'Post form for adding Doctor'
    var name_row = create_input_element('doctor_name', 'maximum 20 symbols', 'Doctor name', 'name_row', 'doctor_name')
    var patricity_row = create_input_element('doctor_patricity', 'maximum 20 symbols', 'Doctor patricity', 'patricity_row', 'doctor_patricity')
    var surname_row = create_input_element('doctor_surname', 'maximum 20 symbols', 'Doctor surname', 'surname_row', 'doctor_surname')
    var select_speciality = create_select_element(specialities, 'speciality', 'choise a doctor speciality', 'Doctor speciality', 'speciality_row', 'doctor_speciality')
    var buttons = create_buttons([['submit', ['btn', 'btn-dark']], ['reset', ['btn', 'btn-outline-danger']]])
    document.getElementById('main-container').appendChild(header)
    container = document.getElementById('main-container');
    document.getElementById('doctor_header').style.animationName='reverseAnimation';
    document.getElementById('doctor_header').style.animationDuration='500ms';
    document.getElementById('doctor_header').style.animationFillMode='forwards';


    form = document.createElement('div');
    form.id = 'doctor-form'
    form.appendChild(surname_row);
    form.appendChild(name_row);
    form.appendChild(patricity_row);
    form.appendChild(select_speciality);
    form.appendChild(buttons);

    document.getElementById('main-container').appendChild(form);

    document.getElementById('doctor-form').style.animationName='reverseAnimation';
    document.getElementById('doctor-form').style.animationDuration='ms';
    document.getElementById('doctor-form').style.animationFillMode='forwards';
    let submit_button = document.querySelector('#submit_button')
    console.log(submit_button)
    switch(action){
        case 'add':{
            
            submit_button.addEventListener('click', () => post(document.getElementById('doctor-form')))
            console.log('button event add add')
            return;
        }
        case 'upd':{
            
            submit_button.addEventListener('click', () => put(document.getElementById('doctor-form')))
            console.log('button event add upd')
            return;
        }
    }
    
}

function create_input_element(id, description_text, placeholder, row_id, input_name){
    var label = document.createElement('label')
    var input = document.createElement('input')
    var description = document.createElement('small')
    var row = document.createElement('div')
    var col = document.createElement('div')
    row.id = row_id
    col.classList.add('col')
    row.classList.add('row')
    input.id = id
    input.name = input_name
    input.placeholder = 'input ' + placeholder
    input.classList.add('form-control')
    description.innerHTML = description_text
    description.classList.add('form-text')
    description.classList.add('text-muted')
    label.innerHTML = placeholder
    label.classList.add('form-label')
    label.htmlFor = input.getAttribute('id')

    col.appendChild(label)
    col.appendChild(input)
    col.appendChild(description)
    row.appendChild(col)
    return row
}

function create_select_element(data, id, description_text, label_text, row_id, select_name){
    var label = document.createElement('label')
    var select = document.createElement('select')
    var description = document.createElement('small')
    var row = document.createElement('div')
    var col = document.createElement('div')

    select.classList.add('form-select')
    select.id = id
    select.name = select_name
    label.htmlFor = id
    label.innerHTML = label_text
    label.classList.add('form-label')

    row.classList.add('row')
    row.id = row_id
    col.classList.add('col')

    description.innerHTML = description_text
    description.classList.add('form-text')
    description.classList.add('text-muted')

    for (elem of data){
        select_option = document.createElement('option')
        select_option.innerHTML = elem['doctor_speciality_name'];
        select_option.value = elem['doctor_speciality_id'];
        select.appendChild(select_option)
    }
    col.appendChild(label)
    col.appendChild(select)
    col.appendChild(description)
    row.appendChild(col)
    return row
}

function create_buttons(types){
    var row = document.createElement('div')
    let col = document.createElement('div')
    col.classList.add('col')
    row.classList.add('row')

    for (type of types){
        var button = document.createElement('button');
        for (button_class of type[1]){

            button.classList.add(button_class);
        }
        button.innerHTML = type[0] + ' form';
        button.type = type[0];
        button.id = type[0] + '_button'
        col.appendChild(button)
        row.appendChild(col)
    }
    return row;
}

function get_selected_row_data(){
    tr_arr = document.getElementsByTagName('tr')
    console.log(tr_arr)
    for (tr of tr_arr){
        if (tr.style.backgroundColor == 'rgb(236, 236, 236)')
            return tr
    }
}

function fill_doctor_form(td_array){
    var f = ()=>{
        console.log(td_array)
        var select = document.getElementById('speciality');
        for(option of select.children){
            if(option.innerHTML == td_array.item(4).innerHTML)
                return option.value
        }
    }
    document.getElementById('doctor_surname').value=td_array.item(1).innerHTML;
    document.getElementById('doctor_name').value = td_array.item(2).innerHTML;
    document.getElementById('doctor_patricity').value = td_array.item(3).innerHTML;
    document.getElementById('speciality').value = f.call();
    row = document.createElement('div');
    row.classList.add('row');
    col = document.createElement('div');
    col.classList.add('row');
    
    id = document.createElement('input');
    id.type='hidden'
    id.name='doctor_id'
    id.value=td_array.item(0).innerHTML;
    col.appendChild(id);
    row.appendChild(col);
    parent_div = document.getElementById('speciality_row').parentNode;
    parent_div.insertBefore(row, document.getElementById('speciality_row'));
}