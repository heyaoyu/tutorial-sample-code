function WebSocketDemo(){
    var socket = new WebSocket("ws://localhost:8888/websocket_service");
    socket.onmessage = function(event){
        alert("FromWebSocketServer: "+event.data);
    };
    socket.onopen = function(){
        alert("WebSocket Connection is established.");
        if(socket.readyState == WebSocket.OPEN){
            socket.send("Hello..");
        }
    };
    socket.onerror = function(){
        alert("WebSocket Connection error.");
    };
    socket.onclose = function(){
        alert("WebSorkce Connection is closed.");
    };
}

function main(){
    WebSocketDemo();
}

(main)();