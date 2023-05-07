// W1D3.js
/* 
*/

/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Consider using .split first if you need to, then try to do it without
  ( see https://www.w3schools.com/jsref/jsref_split.asp )
*/

const str1 = "object oriented programming";
const expectedA = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expectedB = "APIE";

const str3 = "software development life cycle";
const expectedC = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expectedD = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
 function acronymize(str) {
    let result = '';
    let lastChar = ' ';
    for(char of str) {
        if (lastChar == ' ' && char != ' ') {
            result += char;
        }
        lastChar = char
    }
    return result.toUpperCase();
}



// console.log(acronymize(str1)); // Expected: "OOP"
// console.log(acronymize(str2)); // Expected: "APIE"
// console.log(acronymize(str3)); // Expected: "SDLC"
// console.log(acronymize(str4)); // Expected: "GIT"


//TEST CODE
const tests = [
    [str1, expectedA],  // tests[0] -> str1 is tests[0][0] & expected1 is tests[0][1]
    [str2, expectedB],
    [str3, expectedC],
    [str4, expectedD]
];
// Replace 'foo' with daily Algo
tests.forEach(x => {
    console.log(`Expected: "${x[1]}", Actual: "${acronymize(x[0])}"`);
})
