var name = "window global name";

function closure(){

    var obj1 = {
        name: "obj1 name",
        getNameFunc: function(){
            return function(){
                return this.name;
            }
        }
    }

    var obj2 = {
        name: "obj2.name",
        getNameFunc: function(){
            var that = this;
            return function(){
                return that.name;
            }
        }
    }

    console.log(obj1.getNameFunc()());

    console.log(obj2.getNameFunc()());

}

function main(){

    closure();

}

(main)();