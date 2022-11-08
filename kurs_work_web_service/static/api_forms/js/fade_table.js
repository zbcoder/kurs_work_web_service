

function fade_table(table){
    tb = document.getElementById('doctor_table').rows
    console.log(tb, tb.length)

    document.getElementById('doctor_table').style.animationName='myAnimation';
    document.getElementById('doctor_table').style.animationDuration='850ms';
    document.getElementById('doctor_table').style.animationFillMode='forwards';

    document.getElementById('pagination-buttons').style.animationName='myAnimation';
    document.getElementById('pagination-buttons').style.animationDuration='850ms';
    document.getElementById('pagination-buttons').style.animationFillMode='forwards';

    document.getElement
    for(i = tb.length-1; i >= 0; i--){
        tb.item(i).style.animationName = 'myAnimation';
        tb.item(i).style.animationDuration = '850ms';
        tb.item(i).style.animationFillMode='forwards'
    }
    setTimeout(remove_table, 900)
    setTimeout(show_create_form, 900)
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
/*window.onanimationend = e => {

}*/
function show_create_form(){

    var header = document.createElement('h4')
    header.id = 'doctor_header'
    header.innerHTML = 'Post form for adding Doctor'
    var name_row = createInputElement('doctor_name', 'maximum 20 symbols', 'Doctor name', 'name_row')
    var patricity_row = createInputElement('doctor_patricity', 'maximum 20 symbols', 'Doctor patricity', 'patricity_row')
    var surname_row = createInputElement('doctor_surname', 'maximum 20 symbols', 'Doctor surname', 'surname_row')
    document.getElementById('main-container').appendChild(header)

    document.getElementById('doctor_header').style.animationName='reverseAnimation';
    document.getElementById('doctor_header').style.animationDuration='500ms';
    document.getElementById('doctor_header').style.animationFillMode='forwards';

    document.getElementById('main-container').appendChild(name_row)

    document.getElementById('name_row').style.animationName='reverseAnimation';
    document.getElementById('name_row').style.animationDuration='625ms';
    document.getElementById('name_row').style.animationFillMode='forwards';

    document.getElementById('main-container').appendChild(patricity_row)

    document.getElementById('patricity_row').style.animationName='reverseAnimation';
    document.getElementById('patricity_row').style.animationDuration='750ms';
    document.getElementById('patricity_row').style.animationFillMode='forwards';

    document.getElementById('main-container').appendChild(surname_row)

    document.getElementById('surname_row').style.animationName='reverseAnimation';
    document.getElementById('surname_row').style.animationDuration='875ms';
    document.getElementById('surname_row').style.animationFillMode='forwards';
}

function createInputElement(id, description_text, placeholder, row_id){
    var label = document.createElement('label')
    var input = document.createElement('input')
    var description = document.createElement('small')
    var row = document.createElement('div')
    var col = document.createElement('div')
    row.id = row_id
    col.classList.add('col')
    row.classList.add('row')
    input.id = id
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