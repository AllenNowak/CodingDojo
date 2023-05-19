/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/
// quarter = 25 cents, dime = 10, nickel = 5, penny = 1
const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * @param {number} cents
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */

 function fewestCoinChange(cents) {
    denoms = [25, 10, 5]
    denoms = { 'quarter': 25, 'dime' : 10, 'nickel': 5, 'penny': 1 }
    let result = {}
    for(coin of denoms) {
        if (cents == 0) {
            return result
        }
        // doublecheck that we can divide by each denom b4 adding

    }
    return result;
}

console.log(fewestCoinChange(cents1)) // { quarter: 1 }
console.log(fewestCoinChange(cents2)) // { quarter: 2 }
console.log(fewestCoinChange(cents3)) // { nickel: 1, penny: 4 }
console.log(fewestCoinChange(cents4)) // { quarter: 3, dime: 2, penny: 4 }


function fewestCoinChange(cents) {
    let results = {}
    const denom = {'quarter': 25, 'dime' : 10, 'nickel' : 5, 'penny' : 1}
    let temp = cents
    let coins = 0
    for (let [key, val] of Object.entries(denom)) {
     if (temp == 0) {
         return results
     }
     // protect against an empty coin
     coins = Math.floor( temp/val )
     if (coins > 0) {
         results [key] = coins
     }
     temp = coins % val
    }
 
    return results
 }



