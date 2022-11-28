async function put_function(url, json){
    console.log(JSON.stringify(json))
    const request_options = {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
            body: JSON.stringify(json)
    }
    const response = await fetch(url+'/', request_options)
    .then((response)=>{
        location.reload();
        return response.json();
    })
    .then((data)=>{
        console.log(data)
    })
    .catch((err)=>{
        console.log(err)
    })
}