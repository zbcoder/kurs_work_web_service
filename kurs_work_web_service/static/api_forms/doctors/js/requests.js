async function post(form_id, url){
    json = generate_json(form_id, 4)
    const response = await fetch(url, {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
    body: JSON.stringify(json)
  });
  clone_response = response.clone()
  if (clone_response.statusText=='Created'){
    notification = 'Doctor was successfully created'
    flag = true
  }
  else{
       notification = 'Bad request. Try later'
       flag = false
  }
  alert(notification)
  if (flag==true){
    location.reload();
  }
  return response.json();
}

function generate_json(form_id, rows){
    json = {}
    for(i= 0; i<rows; i++){
    var datum;
        datum = form_id.children[i].querySelector('input')
        if(!datum)
            datum = form_id.children[i].querySelector('select')
        if(!json[datum.name]){
            json[datum.name] = '';
        }
        try{
            json[datum.name]=datum.value
        }
        catch{
            json[datum.name]=datum.options[sel.selectedIndex].value
        }
    }
    return json;
}

async function put(form_id, url){
  json = generate_json(form_id, 5);
  new_url = url+json["doctor_id"];
  console.log(new_url)
  const response = await fetch(new_url, {
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
  });
  clone_response = response.clone()
  console.log(clone_response)
  if (clone_response.statusText=='Created'){
    notification = 'Doctor was successfully updated'
    flag = true
  }
  else if(clone_response.status== 200){
    notification = 'Doctor was successfully updated'
    flag = true
  }
  else{
      notification = 'Bad request. Try later'
      flag = false
  }
  alert(notification)
  if (flag==true){
    location.reload();
  }
  return response.json();
}

function delete_request(id){
  console.log()
}