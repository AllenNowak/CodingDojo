/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation or capitalization
*/
// RIOT Read Input Output Talk
// #region
// the 'hash' region & 'hash' endregion tags in VSCode can be collapsed when we don't want to look at their interior
const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

const str5 = "abba"
const expected5 = true;
// #endregion


function isPalindrome(str) {
    for (let i = 0, j = str.length-1; i < j; i++, j--) {
        if (str[i] !== str[j]) {
                return false;
        }
    }
    return true;
}
function isPalindrome2(str) {
    let str2 = str;
    str2 = str2.split('').reverse().join('')
    return str2 === str;
}
  //TEST CODE
  const tests = [
    [str1, expected1],  // tests[0] -> str1 is tests[0][0] & expected1 is tests[0][1]
    [str2, expected2],
    [str3, expected3],
    [str4, expected4],
    [str5, expected5]
];

// console.log('isPalindrome v1 vs v2')
tests.forEach(x => {
    console.log(`v1 Expected: "${x[1]}", Actual: "${isPalindrome(x[0])}"`);
    // console.log(`v2 Expected: "${x[1]}", Actual: "${isPalindrome2(x[0])}"`);
})


