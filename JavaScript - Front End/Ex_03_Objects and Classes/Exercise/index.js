// // Example 1
// const originalArray = [1,2,3,4,5];
// const newArray = originalArray.map(num => num + 1);
// console.log(newArray); // Output: [2,3,4,5,6]


// // Example 2
// const arr = [1,2,3,4,5];

// arr.forEach((num, index, array) => {
//   array[index] = num + 1;
// });

// console.log(arr); // Output: [2, 3, 4, 5, 6]

// Example 3
let arr3 = [1,2,3,4,5,6,7];

for (let key of arr3) {
    key = key+1;
}

console.log(arr3)