// Variant 1
function personInfo(firstName, secondName, age) {
    age = Number(age);
    let person = {firstName: firstName, secondName: secondName, age: age};

    return person
}

console.log(personInfo("Peter", "Pan", "20"));

// Variant 2
function personInfo(firstName, secondName, age) {
    age = Number(age);
    // JS will make keys with the given names(below) and if there are also variables with this names will take their values: 
    let person = {firstName, secondName, age};

    return person
}

console.log(personInfo("Peter", "Pan", "20"));