var EventUtil = {

    addEventHandler: function(element, type, handler){
        if(element.addEventListener){
            element.addEventListener(type, handler, false);
        }else if(element.attachEvent){
            element.attachEvent('on'+type, handler);
        }else{
            element["on"+type] = handler;
        }
    },

    removeEventHandler: function(element, type, handler){
        if(element.removeEventListener){
            element.removeEventListener(type, handler, false);
        }else if(element.detachEvent){
            element.detachEvent('on'+type, handler);
        }else{
            element["on"+type] = null;
        }
    },

    getEvent: function(event){
        return event? event: window.event;
    },

    getTarget: function(event){
        return event.target || event.srcElement;
    },

    preventDefault: function(event){
        if(event.preventDefault){
            event.preventDefault();
        }else{
            event.returnValue = false;
        }
    },

    stopPropagation: function(event){
        if(event.stopPropagation){
            event.stopPropagation();
        }else{
            event.cancelBubble = true;
        }
    }

}

function main(){
    var div = document.getElementById("forEvent");
    if(div){
        EventUtil.addEventHandler(div, 'click', function(event){
            var that = this;
            console.log(that.getAttribute("name"));
            var ent = EventUtil.getEvent(event);
            console.log(ent.type);
            var target = EventUtil.getTarget(event);
            console.log("target==that: "+(target == that));
            EventUtil.removeEventHandler(that, 'click', arguments.callee);
        });
    }
}

EventUtil.addEventHandler(window, 'load', function(){
   main();
});