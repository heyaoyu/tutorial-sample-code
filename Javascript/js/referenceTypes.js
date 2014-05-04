function _object(){
    var person = new Object();
    person.name = "Nico";
    person.age = 29;

    var person2 = {
        "name" : "Nico",
        "age" : 29
    }

    function displayNameAndAge(obj){
        if(typeof obj.name == "string"){
            console.log("The name is "+obj.name);
        }
        if(typeof obj.age == "number"){
            console.log("The age is "+obj.age);
        }
    }

    displayNameAndAge(person);
    displayNameAndAge(person2);
}

function _array(){
    // Array, pop push as Stack, push shift or unshift pop as List
    var colors = "blue,yellow".split(",");
    console.log("The length of Array colors is "+colors.length);
    console.log(colors.toString());
    var count = colors.push("red", "green");
    console.log("The length of Array colors is "+count+" after pushing \"red\" and \"green\".");
    console.log(colors.toString());
    var color = colors.pop();
    console.log("The length of Array colors is "+colors.length+" after popping.");
    console.log("The popped color is "+color);
    console.log(colors.toString());
    color = colors.shift();
    console.log("The length of Array colors is "+colors.length+" after shifting.");
    console.log("The shiftted color is "+color);
    console.log(colors.toString());
    colors.unshift("black", "brown");
    console.log("The length of Array colors is "+colors.length+" after unshifting black and brown.");
    console.log(colors.toString());
    var newColors = colors.concat(["white"]);
    console.log("The length of Array newColors is "+newColors.length+" after concatting white.");
    console.log(newColors.toString());
    var newColors = colors.slice(1,4);
    console.log("colors slicing 1,4 is "+newColors.toString());
    newColors.splice(1,1,"replcement");
    console.log("colors slicing 1,4 is "+newColors.toString()+" after splicing 1,1,\"replcement\".");

    // iteration
    var arrays = [1,2,3,4,5,6];
    console.log("initail arrays is "+arrays.toString());

    var result = arrays.every(function(item, index, array){
        return item>0;
    });
    console.log("every item>0: "+result);
    result = arrays.every(function(item, index, array){
        return item>4;
    })
    console.log("every item>4: "+result);

    result = arrays.filter(function(item, index, arrsy){
       return item%2 == 1;
    });
    console.log("filter item%2==1: "+result);

    arrays.forEach(function(item, index, array){
       console.log("forEach item: "+item+" index: "+index);
    });

    result = arrays.map(function(item, index, array){
       return item*2;
    });
    console.log("map item*2: "+result);

    result = arrays.some(function(item, index, array){
       return item>4;
    });
    console.log("some item >4: "+result);

    console.log("current arrays is "+arrays.toString());
    result = arrays.reduce(function(x, y){
       return x+y;
    });
    console.log("reduce array x+y is "+result);
}

function _date(){
    var start = new Date()
    for(i=0;i<10000000;i++){
        ;
    }
    var end = new Date();
    console.log("iterate 10000000 times cost "+ (end-start)+" millseconds.");
}

function _regexp(){
    var expression = /pattern/gim;
    console.log(expression instanceof RegExp);

    var exp1 = /\[bc\]at/i; // match [bc]at
    var exp2 = new RegExp("\\[bc\\]at", "i") // the same as exp1 but with complex string.

    var exp = /(..)or(.)/; // if with "g", matches will fail..
    var str = "This is a short sentence.";
    console.log(exp.test(str));

    console.log(RegExp.$0);
    console.log(RegExp.$1);
    console.log(RegExp.$2);

    var matches = exp.exec(str);
    console.log(matches[0]);
    console.log(matches[1]);
    console.log(matches[2]);
}

function _function(){
    
}

function main(){
    _object();
    _array();
    _date();
    _regexp();
}

(main)();