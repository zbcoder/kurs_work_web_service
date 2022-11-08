tr_array = document.getElementsByTagName('tr')

function select_row(row){

    for(tr of tr_array){
        if (tr != row){
            tr.style.backgroundColor = '#ffffff'
        }
        else
        {
            if (row.style.backgroundColor == 'rgb(236, 236, 236)'){
                row.style.backgroundColor = '#ffffff'
                document.getElementById('del_button').style.display='none'
                document.getElementById('upd_button').style.display='none'
            }
            else{
                document.getElementById('current_id').value = row.getElementsByTagName('td')[0].innerHTML
                row.style.backgroundColor = 'rgb(236,236,236)'
                document.getElementById('del_button').style.display='block'
                document.getElementById('upd_button').style.display='block'
            }
        }
    }
}