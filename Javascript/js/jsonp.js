/*
*
* jsonp --> same-origin policy: Read: Deny, Write: Limit, Execute: Allow
*
* */

function jsonp(){
    var script = document.createElement("script");
    script.src = "http://localhost:8888/jsonp_service";
    document.getElementsByTagName('head')[0].appendChild(script);
}

function callback(server_str){
    console.log("server_string: "+server_str["str"]);
}

function main(){
    jsonp();
}

(main)();