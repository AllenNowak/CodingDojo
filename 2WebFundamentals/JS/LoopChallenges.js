//LoopChallenge.js
//WebFundamentals Apr23

/**
* Prints to Stdout all odd integers from lower to upper inclusive
 * @param {number} lower
 * @param {number} upper
 * @returns {Array<Number>}
 */
function getOddsBetween(lower, upper) {
    var oddsList = []
    
    for(var i = lower; i<= upper; i++) {
        if(i % 2 == 1) {
            oddsList.push(i)
        }
    }
    return oddsList;
}

var start = 1
var end = 20
var actual = getOddsBetween(start, end);
var actualStr = `The odd numbers from ${start} to ${end} are ${actual}`
var expected = 'The odd numbers from 1 to 20 are 1,3,5,7,9,11,13,15,17,19'
console.log('\nPrinting Odds from 1 to 20')
console.log(actualStr)
console.log('Test', (actualStr === expected) ? 'passed' : 'failed' )




/**
 * Prints all positive integers divisible by a factor lesser than the given bounding value
 * @param {number} factor - the divisor to use
 * @param {number} bound - the largest number we're examining
 * @return {string} a string listing the decreasing multiples
 */
function decreasingMultiplesOfX(divisor, upperBound) {
    const columnWidth = upperBound.toString().length
    var multiples = []
    for(var i=upperBound; i>=divisor; i--) {
        if(i % divisor === 0) {
            multiples.push(i)
        }
    }

    return `The positive multiples of ${divisor} less than ${upperBound} are: ${multiples}.`
}
console.log('\nDecreasing Multiples of 3 from 100 to 0')
console.log(decreasingMultiplesOfX(3, 100));



/**
 * Given a sequence, and using a loop, console.log the values from the sequence
 * @param {Array<Number>}
 */
function logOutThisSequence(sequence) {
    console.log('The sequence is: ')
    for(var i=0; i<sequence.length; i++) {
        console.log(sequence[i])
    }
}
console.log('\nPrint the sequence using a loop')
logOutThisSequence([4, 2.5, 1, -0.5, -2, -3.5])



/**
 * @typedef {Object} SigmaResult
 * @property {number} sum - The Sigma sum
 * @property {string} summary - The string describing the summation
 */
/**
 * Sigma
 * Sum the values from 1..100, then log out the total
 * Here, I'm just playing.  Illustrating a while() for a change of pace
 * and working in a js object for fun.  IRL, I'd just use array.reduce() to get the sum
 * @param {number} start
 * @param {number} end
 * @returns {SigmaResult}
 */
function sigma(start, end) {
    var total = 0
    var resultString = ''
    var index = start
    while (index <= end) {
        resultString += index + ((index < end) ? ' + ' : ' = ')
        total += index
        index++
    }
    resultString += total

    return {sum: total, summary: resultString}
}
var actual = sigma(1, 100)
var summary = actual.summary
var sum = actual.sum
const expectedSum = 5050

console.log('\nSigma sum from 1 to 100')
console.log(summary)
console.log('Sigma Test', (sum === expectedSum) ? 'passed' : 'failed')



/**
 * @param {number} num
 * @returns {number} by definition, f(i) === 1, for i === 0 or 1
 *                      for i > 1, f(i) === i * f(i - 1)
 */
function factorial(num) {
    var factorial = 1
    for(var i = 1; i <= num; i++) {
        factorial *= i
    }

    return factorial
}


var expectedFactorial = 479001600
var factorial12 = factorial(12)
var leftHandSide  = ''
for(var i = 1; i<12; i++) {
    leftHandSide += (i) + ' * '
}
leftHandSide += (i + ' =')
console.log('\nCompute and display !12')
console.log(leftHandSide,factorial12)
console.log('Factorial test', (expectedFactorial===factorial12) ? 'passed' : 'failed')
