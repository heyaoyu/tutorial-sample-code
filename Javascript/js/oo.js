function literalObject(){ // every object duplicate code.
    var person = {
        name: "yaoyu",
        age: 27,
        sayName: function(){
            console.log("literalObject: "+this.name);
        }
    }
    person.sayName();
}

function factoryObject(){ // cannot identify type. instanceof
    function createPerson(name, age){
        var o = new Object();
        o.name = name;
        o.age = age;
        o.sayName = function(){
            console.log("factoryObject: "+this.name);
        }
        return o;
    }
    var person = createPerson("yaoyu", 27);
    person.sayName();
}

function constructorObject(){// same function multiple instances.
    function Person(name, age){
        this.name = name;
        this.age = age;

        this.sayName = function(){
            console.log("constructorObject: "+this.name);
        }
    }

    var person = new Person("yaoyu", 27);
    person.sayName();

    Person("window", "??");// no "new" is window
    window.sayName();
}

function prototypeObject(){// attributes share problem
    function Person(){}

    Person.prototype.name = "yaoyu";
    Person.prototype.age = 27;
    Person.prototype.sayName = function(){
        console.log("prototypeObject: "+this.name);
    }

    var p1 = new Person();
    p1.sayName();
    var p2 = new Person();
    p2.sayName();

    Person.prototype = {
        sayName: function(){
            console.log("cut prototype loose ^_^");
        }
    }

    p1.sayName(); // still the same.
}

function hybridObject(){
    function Person(name, age){
        this.name = name;
        this.age = age;
    }

    Person.prototype.sayName = function(){
        console.log("hybridObject: "+this.name);
    }

    var person = new Person("yaoyu", 27);
    person.sayName();
    var p2 = new Person("susan", 18);
    p2.sayName();
    console.log("sayName function same? "+(person.sayName == p2.sayName));
}


function prototypeExtend(){// super attribute share problem
    function SuperType(){
        this.superValue = true;
    }

    SuperType.prototype.getSuperValue = function(){
        return this.superValue;
    }

    function SubType(){
        this.subValue = false;
    }

    //extend
    SubType.prototype = new SuperType();

    SubType.prototype.getSubValue = function(){
        return this.subValue;
    }

    var instance = new SubType();
    console.log("instance.getSuperValue() is "+instance.getSuperValue());
}

function hybridExtend(){
    function SuperType(colors){
        this.colors = colors;
    }

    SuperType.prototype.getColors = function(){
        return this.colors;
    }

    function SubType(colors){
        // extend attributes
        SuperType.call(this, colors);
        this.other = "other";
    }

    // extend functions
    SubType.prototype = new SuperType();
    SubType.prototype.constructor = SubType;

    SubType.prototype.sayColors = function(){
        console.log("colors: "+this.colors);
    }

    var instance = new SubType(["red", "green"]);
    instance.sayColors();
}

function main(){
    literalObject();
    factoryObject();
    constructorObject();
    prototypeObject();
    hybridObject();

    prototypeExtend();
    hybridExtend();
}

(main)();