/*
*
* two ways of comet. long polling or streaming line
*
* */


function main(){
    var xhr = createXHR();
    var dataStart = 0;
    xhr.open("get", "/comet_service", true);
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 3){ // important, some data get will be 3
            var data = xhr.responseText.substring(dataStart);
            alert(data);
            dataStart += data.length;
        }
    }
    xhr.send(null);
}

(main)();