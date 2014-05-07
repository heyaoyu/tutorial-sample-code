/*
*
* Ajax in panel2.html will fail cause same-origin policy.
*
* */
function createXHR(){
    if(typeof XMLHttpRequest != undefined){
        xhr = new XMLHttpRequest();
    }else{
        throw Error("No XHR or no support IE.");
    }
    return xhr;
}

function getExample(){
    var xhr = createXHR();
    xhr.onreadystatechange = function(){
        if(xhr.readyState==4){
            if((xhr.status >= 200 && xhr.status < 300) || xhr.status == 304){
                alert(xhr.responseText);
            }else{
                alert("Request was unsuccessful: "+xhr.status);
            }
        }
    }
    xhr.open("get", "/", true);
//    xhr.setRequestHeader("header":"value");
    xhr.send(null);
}

function postExample(){
    var xhr = createXHR();
    xhr.onreadystatechange = function(){
        if(xhr.readyState==4){
            if((xhr.status >= 200 && xhr.status < 300) || xhr.status == 304){
                alert(xhr.responseText);
            }else{
                alert("Request was unsuccessful: "+xhr.status);
            }
        }
    }
    xhr.open("post", "/post_service", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send("arg=argValue");
}

function main(){
    getExample();
    postExample();
}

(main)();