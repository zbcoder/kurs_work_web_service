//not working without bootstrap

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

function create_multy_row(cols, small_text, label_text, input_name, input_id, placeholders, type, max=[], min=[]){
    var row = document.createElement('div')
    row.classList.add('row')
    var label = document.createElement('label')
    label.innerHTML = label_text;
    label.classList.add('form-label')

    row.appendChild(label)

    for(i = 0; i<cols; i++){
        var col = document.createElement('div')
        col.classList.add('col')

        var input = document.createElement('input')
        input.type=type
        input.classList.add('form-control')
        input.id=input_id[i]
        input.name=input_name[i]
        input.placeholder=placeholders[i]
        try{
            input.max=max[i]
            input.min=min[i]
        }
        catch{
            input.max=0;
            input.min=0;
        }
        var small = document.createElement('small');
        small.innerHTML = small_text[i]
        small.classList.add('form-text')
        small.classList.add('text-muted')

        col.appendChild(input);
        col.appendChild(small);

        row.appendChild(col)
    }
    return row;
}