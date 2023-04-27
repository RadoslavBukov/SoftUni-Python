function employeesAndPersonalNumbers(arr) {
    // let employees = {}
    // for (const name of arr) {
    //     employees[name] = name.length;
    // }
    // Same as above
    let employees = arr.reduce((data, employee) => {
        data[employee] = employee.length;
        return data;
    }, {});

    for (const key in employees) {
        console.log(`Name: ${key} -- Personal Number: ${employees[key]}`)
    }
}

employeesAndPersonalNumbers(
    [
        'Silas Butler',
        'Adnaan Buckley',
        'Juan Peterson',
        'Brendan Villarreal'
    ]        
)