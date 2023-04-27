function convertToJSON( firstName, lastName, haircolor){
    let person = {firstName, lastName, haircolor};
    let jsonString = JSON.stringify(person);
    console.log(jsonString);
}

convertToJSON('George', 'Jones', 'Brown')