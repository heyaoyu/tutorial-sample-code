/*
*
* two ways of comet. long polling or streaming line
*
* */


function main(){
    var xhr = createXHR();
    xhr.open("get", "/comet_service", true);
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 3 || xhr.readyState == 4){ // important, some data get will be 3
            alert(xhr.responseText);
        }
    }
    xhr.send(null);
}

(main)();