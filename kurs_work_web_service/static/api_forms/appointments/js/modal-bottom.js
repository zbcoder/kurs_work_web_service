const modal = document.querySelector(".modal-bottom");
const overlay = document.querySelector(".overlay");
const closeModalBtn = document.querySelector("#modal-bottom-close-btn");
const closeModalBtn2 = document.querySelector("#modal-bottom-cancel-button");
const submitBtn = document.querySelector("#modal-bottom-submit-button");
const openModalBtn = document.querySelector("#create_button");
const openUpdateModal = document.querySelector("#upd_button");
var thisForm = document.querySelector("#appointments_form"); 

function get_selected_row_data(){
    tr_arr = document.getElementsByTagName('tr')
    for (tr of tr_arr){
        if (tr.style.backgroundColor == 'rgb(236, 236, 236)')
            return tr
    }
}

const submit_action = async function(json){
    tr = get_selected_row_data()
    console.log(tr.children.item(0).innerHTML)
    const response = await fetch('http://127.0.0.1:8000/api_root/appointments-list/'+tr.children.item(0).innerHTML, {
                method: 'PUT',
                mode: 'cors',
                cache: 'no-cache',
                credentials: 'same-origin',
                headers: {
                            'Content-Type': 'application/json'
                },
                redirect: 'follow',
                referrerPolicy: 'no-referrer',
                body: JSON.stringify(json)
        }).then((response)=>{return response.json()}).then((data)=>{console.log(data)}).catch((err)=>{console.log(err)});
    console.log(response);
    location.reload()
} 
const openModalForPost = function () {
//   tr = get_selected_row_data()
  thisForm.method = "POST"
  setTimeout(modal.classList.remove("hidden"), 900);
  setTimeout(overlay.classList.remove("hidden"), 900);
};
const closeBottomModal = function () {
  setTimeout(modal.classList.add("hidden"), 900);
  setTimeout(overlay.classList.add("hidden"), 900);
};

const update_appointment = function(){
    tr = get_selected_row_data()
    thisForm.method = "PUT"
    thisForm.action = ""
    fill_form(tr)
    setTimeout(modal.classList.remove("hidden"), 900);
    setTimeout(overlay.classList.remove("hidden"), 900);
    thisForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(thisForm)
        const json={
            'date_of_admission': String(formData.get('date_of_admission')),
            'health_complaints': formData.get('health_complaints'),
            'patient': parseInt(formData.get('patient')),
            'doctor': parseInt(formData.get('doctor'))
        }
        console.log(json)
        submit_action(json);
    })
}

function fill_form(tr){
    modal.querySelector('#health-complaints').value= tr.children.item(1).innerHTML
    modal.querySelector('#admission_date').value= tr.children.item(2).innerHTML
    modal.querySelector('#doctor').value= tr.children.item(4).querySelector('input').value
    modal.querySelector('#patient').value= tr.children.item(3).querySelector('input').value
}
openUpdateModal.addEventListener("click", update_appointment);
closeModalBtn.addEventListener("click", closeBottomModal);
openModalBtn.addEventListener("click", openModalForPost);
closeModalBtn2.addEventListener("click", closeBottomModal);
