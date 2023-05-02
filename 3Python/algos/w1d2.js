// W1D2.js
/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
    if (str.length < 2) {
        return str;
    }
    let result = '';
    for (let i = 0; i < str.length; i++) {
         result += str[str.length-1 - i];       // the same as result = result + foo
    }
    
    /*
    Spencer's suggestion
    for (let k = 0; k< str.length-1; k++) {
        result = str[k] + result                // this is result = foo + result
    }
     */
    return result;
}

//TEST CODE FOR REVERSE
const tests = [
    [str1, expected1],  // tests[0] -> str1 is tests[0][0] & expected1 is tests[0][1]
    [str2, expected2],
    [str3, expected3],
    [str4, expected4]
];
tests.forEach(x => {
    console.log(`Expected: "${x[1]}", Actual: "${reverseString(x[0])}"`);
})
// console.log(reverseString(str1)) // Expected: erutaerc
// console.log(reverseString(str2)) // Expected: god
// console.log(reverseString(str3)) // Expected: olleh
// console.log(reverseString(str4)) // Expected: ""


