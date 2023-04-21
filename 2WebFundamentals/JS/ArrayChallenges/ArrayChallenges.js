// WebFundamentals Apr2023
// JS | Advanced Topics | Array Challenges

/* Always Hungry
 * Write a function that is given an array and each time the value is "food" 
    it should console log "yummy". 
    (else) If "food" was not present in the array 
    console log "I'm hungry" once. 
 */
function alwaysHungry(arr) {
    let result = ''
    for( let value of arr) {
        if(value == 'food') {
            result += '"yummy", '
        }
    }

    return result.length === 0 ? `"I\'m hungry"` : result.slice(0, -2)  // Need to remove the trailing ", "
}
  
let result1 = alwaysHungry([3.14, "food", "pie", true, "food"]);
console.log(result1, 'received');
console.log('"yummy", "yummy"', 'expected');
// this should console log "yummy", "yummy"
let result2= alwaysHungry([4, 1, 5, 7, 2]);
console.log(result2, 'received');
console.log('"I\'m hungry"', 'expected');
// this should console log "I'm hungry"

/*
High Pass Filter
Given an array and a value cutoff, return a new array containing only the values larger than cutoff.
 */
function highPass(arr, cutoff) {
    var filteredArr = [];
    filteredArr = arr.filter( x => x > cutoff);
    // for(let x of arr) {
    //     if (x > cutoff) {
    //         filteredArr.push (x)
    //     }
    // }
    
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // we expect back [6, 8, 10, 9]

/*
Better than average
Given an array of numbers return a count of how many of the numbers are larger than the average.
 */
function betterThanAverage(arr) {
    if(arr.length === 0) return 0;

    var sum = 0;
    sum = arr.reduce((a,b) => a + b, 0);
    // calculate the average
    var avg = sum / arr.length;
    // count the values above the average
    var count = arr.filter( val => val > avg).length;

    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // we expect back 4


/*
Array Reverse
Write a function that will reverse the values an array and return them.
 */
function reverse(arr) {
    if(arr.length < 2) return arr;

    for(let i=0; i< ((arr.length-1) / 2); i++) {
        let invrs = (arr.length-1) - i;
        [arr[i], arr[invrs]] = [arr[invrs], arr[i]]
    }

    return arr;
}
   
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]


/*
Fibonacci Array
Fibonacci numbers have been studied for years and appear often in nature. 
Write a function that will return an array of Fibonacci numbers up to a given length n. 
Fibonacci numbers are calculated by adding the last two values in the sequence together. 
So if the 4th value is 2 and the 5th value is 3 then the next value in the sequence is 5.
 */
function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    for(let i=2; i<=n; i++) {
        fibArr.push(fibArr[i-2] + fibArr[i-1])
    }

    return fibArr;
}
   

var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
console.log(fibonacciArray(21));
// expecting: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765, 10946


