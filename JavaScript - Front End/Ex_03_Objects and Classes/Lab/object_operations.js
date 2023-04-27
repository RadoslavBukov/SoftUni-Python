// Object
let person = {firstName: "Lacho", lastName: "Indarov", age:52, colorHair: 'brown', 'My Grades': [2,3,4], info: {email: 'lacho@mail.bg'}, sayHello: function() {
    return `Hello  ${this.firstName} ${this.lastName}`    
} };

console.log(person.sayHello());

// Print object atributes
console.log(person);

console.log(person.name);
console.log(person.age);
console.log(person.colorHair);

console.log(person["My Grades"]);

// First elem of "My grades" array
console.log(person["My Grades"][0]);

// info is nested object in the object person
console.log(person.info.email);

// Change the values of the object
person.name = "Radoslav"

person["My Grades"].push(5);
console.log(person["My Grades"]);
