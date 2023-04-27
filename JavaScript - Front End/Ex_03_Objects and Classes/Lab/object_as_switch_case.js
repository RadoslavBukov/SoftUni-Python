// switch case:
let count = 5;

// switch (command) {
//     case 'increment':
//         count++;
//         break;
//     case 'decrement':
//         count--;
//         break;
//     case 'reset':
//         count = 0;
//         break;
// }


// switch case as object:
const commandParser = {
    increment() { count++; },
    decrement() { count--; },
    reset() { count = 0; }
    // increment: (count) => ++count,
    // decrement: (count) => --count,
    // reset: (count) => 0,
}

count = commandParser.increment(count);
count = commandParser.decrement(count);

console.log(count)