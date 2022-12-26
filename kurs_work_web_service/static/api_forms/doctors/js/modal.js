const modal = document.querySelector(".modal-custom");
const overlay = document.querySelector(".overlay");
const openModalBtn = document.querySelector("#del_button");
const closeModalBtn = document.querySelector(".btn-close");
const closeModalBtn2 = document.querySelector("#modal-cancel-button");
const delButton = document.querySelector("#modal-delete-button");
const url = openModalBtn.value;

console.log(overlay, openModalBtn, closeModalBtn, delButton)


const deleteRow = async function(){
  tr = get_selected_row_data()
  console.log(tr.children.item(0).innerHTML)
  const response = await fetch(url+tr.children.item(0).innerHTML, {
              method: 'DELETE',
              mode: 'cors',
              cache: 'no-cache',
              credentials: 'same-origin',
              headers: {
                        'Content-Type': 'application/json'
              },
              redirect: 'follow',
              referrerPolicy: 'no-referrer',
              body: JSON.stringify({'doctor_id': parseInt(tr.children.item(0).innerHTML)})
    });
  console.log(response);
  location.reload()
} 
const openModal = function () {
  tr = get_selected_row_data()
  setTimeout(modal.classList.remove("hidden"), 900);
  setTimeout(overlay.classList.remove("hidden"), 900);
};
const closeModal = function () {
  setTimeout(modal.classList.add("hidden"), 900);
  setTimeout(overlay.classList.add("hidden"), 900);
};

delButton.addEventListener("click", deleteRow);
closeModalBtn.addEventListener("click", closeModal);
openModalBtn.addEventListener("click", openModal);
closeModalBtn2.addEventListener("click", closeModal);

