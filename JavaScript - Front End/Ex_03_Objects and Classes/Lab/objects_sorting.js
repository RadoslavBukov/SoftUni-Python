let people = {
    'Kiril': {age: 25, email: 'kiril@abv.bg'},
    'Peter': {age: 21, email: 'pesho@abv.bg'},
    'Georgi': {age: 18, email: 'georg@abv.bg'},
}

let entries = Object.entries(people)
let sortedByName = entries.sort((personA, personB) => {
    let personAName = personA[0];
    let personBName = personB[0];
    return personAName.localeCompare(personBName);
});

for (const [name, info] of sortedByName) {
    console.log(name);
    console.log(info);
} 