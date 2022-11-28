function hide_element(element_id){
    document.querySelector('#'+element_id).classList.add('fade')
}

function show_element(element_id){
    document.querySelector('#'+element_id).classList.remove('fade')
}

function back(){
    location.reload()
}

function remove_element(element_id){
    console.log('#'+element_id)
    document.querySelector('#'+element_id).remove();
}

function get_selected_row_data(){
    tr_arr = document.getElementsByTagName('tr')
    console.log(tr_arr)
    for (tr of tr_arr){
        if (tr.style.backgroundColor == 'rgb(236, 236, 236)')
            return tr
    }
}