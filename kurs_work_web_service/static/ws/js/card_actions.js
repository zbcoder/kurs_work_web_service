function show_btn(val){
    var x = document.getElementById('card'+val)
    var y = document.getElementById('1btn'+val)
    var z = document.getElementById('2btn'+val)
    console.log('block')
    y.style.display = 'block'
    z.style.display = 'block'
}


function hide_btn(val){
    var x = document.getElementById('card'+val)
    var y = document.getElementById('1btn'+val)
    var z = document.getElementById('2btn'+val)
    console.log('none')
    y.style.display = 'none';
    z.style.display = 'none';
}

function filter_function() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("doctors_info");
  filter = input.value.toUpperCase();
  table = document.getElementById("doctors_table");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

function show_details(id){
    document.location.href=id
}

function create_str(id){
    console.log('im tut :)')
}