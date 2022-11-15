function get_page_with_page_size(current_page){
    select = document.querySelector('.form-select')
    window.location.href="?page="+current_page+"&page_size="+select.value
}

function set_page_filter(current_page){
    const queryString = window.location.search;
    console.log(queryString)
    const urlParameters = new URLSearchParams(queryString);
    console.log(urlParameters)
}

function insertParam(key, value) {
        key = escape(key); value = escape(value);
        var kvp = document.location.search.substr(1).split('&');
        if (kvp == '') {
            document.location.search = '?' + key + '=' + value;
        }
        else {
            var i = kvp.length; var x; while (i--) {
                x = kvp[i].split('=');

                if (x[0] == key) {
                    x[1] = value;
                    kvp[i] = x.join('=');
                    break;
                }
            }
            if (i < 0) { kvp[kvp.length] = [key, value].join('='); }
            //this will reload the page, it's likely better to store this until finished
            document.location.search = kvp.join('&');
        }
    }


function add_parameter(key, element){
    value = document.getElementById(element).value;
    var params = document.location.search.substr(1).split('&');
    console.log(params)
    if(params==''){
        document.location.search='?'+key+'='+value;
    }
    else{
        search_string = '?'
        for(param of params){
            param_dict=param.split('=')
            if(param_dict[0]!=key)
                search_string+=param_dict[0]+'='+param_dict[1]+'&';
        }
        search_string+=key+'='+value;
        document.location.search=search_string;
    }
}

function keep_params(link){
    var params=link.substr(1).split('?')[1].split('&');
    search_string = '?'
    for(param of params){
        param_dict=param.split('=')
        search_string+=param_dict[0]+'='+param_dict[1]+'&';
    }
    document.location.search=search_string;
}

function create_url(key, page){
    var params = document.location.search.substr(1).split('&');
    if(params==''){
        document.location.search='?'+key+'='+page;
    }
    else{
        search_string = '?'
        for(param of params){
            param_dict=param.split('=')
            if(param_dict[0]!=key)
                search_string+=param_dict[0]+'='+param_dict[1]+'&';
        }
        search_string+=key+'='+page;
        document.location.search=search_string;
    }
   
}