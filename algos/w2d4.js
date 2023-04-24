// Week Two of Web Fundamentals
/**
 * Nested Arrays
 */

const arr1 = [
  [2, 5, 8],
  [3, 6, 1],
  [5, 7, 7],
];
const value1 = 6;
const expected1 = true;

/**
 * Given a two dimensional array, determine if the value is present
 * @param {Array<Array<any>>} arr2d
 * @param {number} value
 * @returns {boolean} true if present, false if not
 */
function isPresent2d(arr2d, value) {
    for(let row of arr2d) {
        for (let col of row) {
            if(col === value) {
                return true;
            }
        }
    }
    return false;
}

const tests = [
    [[[]], value1, false]
    // [[[value1]], value1, true],
    // [arr1, value1, expected1]
];

tests.forEach(x => {
    var actual = isPresent2d(x[0], x[1]);
    var expected = x[2];
    console.log(`With x=[${x[0]}] & ${x[1]}, expected= ${expected} and actual = ${actual}`)
// tests.forEach(x => console.log(isPresent2d(x[0], x[1], x[2])));
// console.log(`isPresent([arr], ${value1}) is ${isPresent2d(arr1, value1)} should be ${expected1}`);
});
/************************************************************************** */

const arr2 = [
  [2, 5, 8],
  [3, 6, 1],
  [5, 7, 7],
];
const expected2 = [2, 5, 8, 3, 6, 1, 5, 7, 7];

/**
 * Given a two dimensional array, return a new array that the contains
 * just the elements of the inner arrays
 * @param {Array<Array<any>>} arr2d
 * @returns {Array<any>} the flattened array
 */
function flattenArray(arr2d) {
    const result = []
    for(let row of arr2d) {
        for(let col of row) {
            result.push(col)
        }
    }
    return result;
}

console.log(expected2)
console.log(flattenArray(arr2))



