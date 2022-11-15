tr_array = document.getElementsByTagName('tr')

function select_row(row){

    for(tr of tr_array){
        if (tr != row){
            if(tr.style.baackgroundColor != 'rgb(51, 51, 51)'){
                tr.style.backgroundColor = '#ffffff'
            }
        }
        else
        {
            if (row.style.backgroundColor == 'rgb(236, 236, 236)'){
                row.style.backgroundColor = '#ffffff'
                off_buttons()
            }
            else{
                document.getElementById('current_id').value = row.getElementsByTagName('td')[0].innerHTML
                row.style.cssText=`background-color: rgb(236, 236, 236);`
                document.getElementById('del_button').classList.remove('disabled')
                document.getElementById('upd_button').classList.remove('disabled')

                document.getElementById('upd_button').style.display='block';
                document.getElementById('del_button').style.display='block';

                document.getElementById('del_button').style.animationName='reverseAnimation';
                document.getElementById('del_button').style.animationDuration='250ms';
                document.getElementById('del_button').style.animationFillMode='forwards';

                document.getElementById('upd_button').style.animationName='reverseAnimation';
                document.getElementById('upd_button').style.animationDuration='250ms';
                document.getElementById('upd_button').style.animationFillMode='forwards';

            }
        }
    }
}

function off_buttons(){
    document.getElementById('del_button').style.animationName='myAnimation';
    document.getElementById('del_button').style.animationDuration='250ms';
    document.getElementById('del_button').style.animationFillMode='forwards';
    document.getElementById('del_button').classList.add('disabled')

    document.getElementById('upd_button').style.animationName='myAnimation';
    document.getElementById('upd_button').style.animationDuration='250ms';
    document.getElementById('upd_button').style.animationFillMode='forwards';
    document.getElementById('upd_button').classList.add('disabled');
}