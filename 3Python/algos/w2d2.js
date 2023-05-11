/* 
  Given a string,
  return a new string with the duplicate characters excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABCabcABCabcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

//bonus
const str5 = "aba"
const expected5 = "ba" // ab

const str6 = 'zohz'
const expected6 = 'ohz'

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
// based Jojo's team's algo from w2d1
// function stringDedupe(str="") {
//     let result = ''
//     let res2 = []
//     for (let i = str.length-1; i >= 0; i-- ) {
//         if( ! res2.includes(str[i])) {      // when we haven't seen arr[i] yet
//             // res2.push(arr[i])
//             res2[ str[i] ] = str[i];        // store that we've seen str[i]
//             result = str[i] + result;       // pre pend this character to the front of the string
//         }
//     }
//     return result
// }

function stringDedupe(str="") {
    let result = ''
    let res2 = []

    // from right to left, so we capture the final copy of any letter
    for (let i = str.length-1; i >= 0; i-- ) {  
    // when we haven't seen this letter yet
    if( ! res2.includes(str[i])) {
            // pre pend it to the front of the return string
            result = str[i] + result;           
            // And store it in our 'seen' bucket
            res2.push(str[i]);
        }
    }

    return result
}


console.log(stringDedupe(str1), '||', expected1);
console.log(stringDedupe(str2), '||', expected2);
console.log(stringDedupe(str3), '||', expected3);
console.log(stringDedupe(str4), '||', expected4);
console.log(stringDedupe(str5), '||', expected5);
console.log(stringDedupe(str6), '||', expected6);



/*
  //TEST CODE
const tests = [
    [str1, expected1],
    [str2, expected2],
    [str3, expected3],
    [str4, expected4],
    [str5, expected5]
];
// Replace 'foo' with daily Algo
tests.forEach(x => {
    console.log(`Expected: "${x[1]}", Actual: "${makeFrequencyTable(x[0])}"`);
})
*/





