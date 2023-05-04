function shoppinglist(input) {
    shoppingListCollection = input.shift().split("!");

    for (row in input){
        [command, product] = row.split(" ");
        if (command === "Urgent"){

        }
        if (command === "Unnecessary"){
            
        }
        if (command === "Correct"){
            
        }
        if (command === "Rearrange"){
            
        }
    }
}





shoppinglist(
    (["Tomatoes!Potatoes!Bread",
"Unnecessary Milk",
"Urgent Tomatoes",
"Go Shopping!"])
)