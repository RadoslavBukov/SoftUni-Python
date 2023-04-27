let person = {name: "Lacho"};
let arr = [person, {name: "Kiro"}, {name: "Georgi"}];

// Find object in array by name
let foundPerson = arr.find((p) => p.name === person.name);
console.log(foundPerson);

// Find object in array by index
let indexOfFound = arr.findIndex((p) => p.name === person.name);
console.log(arr[indexOfFound]);

