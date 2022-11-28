const del_modal = document.querySelector(".modal-custom");
const btnOpenModal = document.querySelector("#del_button");
const btnCloseModal = document.querySelector("#btn-close");
const closeModal2 = document.querySelector("#modal-cancel-button");
const delButton = document.querySelector("#modal-delete-button");

console.log(overlay, openModalBtn, closeModalBtn, delButton)


const deleteRow = async function(){
  tr = get_selected_row_data()
  console.log(tr.children.item(0).innerHTML)
  const response = await fetch('http://127.0.0.1:8000/api_root/appointments-list/'+tr.children.item(0).innerHTML, {
              method: 'DELETE',
              mode: 'cors',
              cache: 'no-cache',
              credentials: 'same-origin',
              headers: {
                        'Content-Type': 'application/json'
              },
              redirect: 'follow',
              referrerPolicy: 'no-referrer',
              body: JSON.stringify({'doctor_appointment_id': parseInt(tr.children.item(0).innerHTML)})
    });
  console.log(response);
  location.reload()
} 
const openModal = function () {
  tr = get_selected_row_data()
  setTimeout(del_modal.classList.remove("hidden"), 900);
  setTimeout(overlay.classList.remove("hidden"), 900);
};
const closeModal = function () {
  setTimeout(del_modal.classList.add("hidden"), 900);
  setTimeout(overlay.classList.add("hidden"), 900);
};

delButton.addEventListener("click", deleteRow);
btnCloseModal.addEventListener("click", closeModal);
btnOpenModal.addEventListener("click", openModal);
closeModal2.addEventListener("click", closeModal);

