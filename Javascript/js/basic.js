function sayScript(){
    alert("<\/script>");
}

function dataTypes(){
    console.log(typeof(1));
    console.log(typeof(true));
    console.log(typeof("1"));
    var age;
    console.log(typeof(age));
    console.log(typeof(null));
    console.log("number? "+(isNaN("I am a Number... :D")?"No":"Yes"));
}

function expressions(){
    var x=4, y=2;
    console.log("x*y="+(x*y));
    console.log("x+y="+(x+y));
    console.log("++x is "+(++x));
    console.log("the bigger number is "+(x>y?x:y));
    console.log("\"55\" == 55 ? "+("55"==55));
    console.log("\"55\" === 55 ? "+("55"===55));
    console.log("undefined == null ? "+(undefined==null));
    console.log("undefined === null ? "+(undefined===null));
}

function funcArgumensts(){
    console.log("arguments.callee is "+arguments.callee);
    console.log("There are "+arguments.length+" arguments.");
}

function passByValue(){

    function addTen(num){
        num += 10;
        return num;
    }

    function setName(obj){
        obj.name = "Nico";
    }

    var num = 10;
    console.log("num before: "+num);
    addTen(num);
    console.log("num after: "+num);

    var obj = new Object();
    console.log("obj.name before: "+obj.name);
    setName(obj);
    console.log("obj.name after: "+obj.name);
}

function dataInstnaces(){
    var obj = new Object();
    console.log("obj instanceof Object is "+(obj instanceof Object));
    console.log("obj instanceof Array is "+(obj instanceof Array));
}

function main(){
    sayScript();
    dataTypes();
    expressions();
    funcArgumensts("string");
    funcArgumensts("string", 1 , true);
    passByValue();
    dataInstnaces();
}

(main)();
