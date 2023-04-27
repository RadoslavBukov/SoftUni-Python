// Correct write of object:
let person = {
    firstName: "Lacho", 
    lastName: "Indarov", 
    age:52, 
    colorHair: 'brown', 
    'My Grades': [2,3,4], 
    info: {email: 'lacho@mail.bg'}, 
    sayHello: function() {
        return `Hello ${this.firstName} ${this.lastName}`
    },
// can register function, without *name*: function()
    sayGoodbye() {
        return `Goodbye ${this.firstName} ${this.lastName}`
    } 
};

console.log(person.sayHello());

// Take all key, values:

// Variant 1: with forEach function of array
const tuples = Object.entries(person)
    .forEach(([key, value]) => console.log(key, value));

// with for-of cycle (transforming keys, values in array)
const tuples2 = Object.entries(person);
for (const [key, value] of tuples2) {
    console.log(`Key: ${key}`);
    console.log(`Value: ${value}`);
}

// with for-in cycle (iterating the object)
for (const [key, value] in person) {
    console.log(key);
    console.log(person[key]);
}
