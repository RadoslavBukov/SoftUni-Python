class Student {
    constructor (name, age, grades) {
        this.name = name;
        this.age = age;
        this.grades = grades;
    }

    sayHello() {
        console.log(`My name is ${this.name}`);
    }
}

const student1 = new Student('Kiril', 25, [3,4,5]);
const student2 = new Student('Georgi', 26, [4,4,6]);
const student3 = new Student('Peter', 27, [6,4,5]);

student1.sayHello();

// chech type of variable
console.log(typeof Student);



// class could be written as a function - function constructor
function Student2(name, age, grades) {
        this.name = name;
        this.age = age;
        this.grades = grades;
}

Student2.prototype.sayHello = function() {
    console.log(`Hello ${this.name}`);
}

const student5 = new Student2('Lacho', 56, [2,2,2,3]);
console.log(student5);
student5.sayHello();
