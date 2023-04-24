/* 
  Given an array of integers
  return the index where the smallest integer is located

  return -1 if there is no smallest integer (array is empty) 
  since -1 is not a valid index, this indicates it couldn't be found

  If the smallest integer occurs more than once, return the index of the first one.
*/

const nums1 = [5, 2, 3];
const expected1 = 1;

const nums2 = [5, 4, 2, 2, 3];
const expected2 = 2;

const nums3 = [];
const expected3 = -1;

/**
 * Returns the index of the smallest number from the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} Index of smallest number or -1 if empty given array.
 */
function indexOfMinVal(nums) {
    if(nums.length === 0) return -1;
    
    let result = {index:0, value:nums[0]}
    for (let i = 0; i < nums.length; i++) {
        if(nums[i] < result.value) {
            result = {index: i, value: nums[i]}
        } 
    }
    return result.index;
}

console.log('minimum index of: ', nums1, ' is', indexOfMinVal(nums1), ' expected:', expected1 );
console.log('minimum index of: ', nums2, ' is', indexOfMinVal(nums2), ' expected:', expected2 );
console.log('minimum index of: ', nums3, ' is', indexOfMinVal(nums3), ' expected:', expected3 );


/*******************************************************************************/

/* 
  Given an array, reverse it's items in place
  return the array after reversing it

  Do it in place without using any built in methods
*/

const arr1 = [1, 2, 3];
const expected1a = [3, 2, 1];

const arr2 = ['a', 'b'];
const expected2a = ['b', 'a'];

const arr3 = ['a'];
const expected3a = ['a'];

const arr4 = [];
const expected4a = [];

/**
 * Reverses the given arr in place without built in methods
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} items
 * @returns {Array<any>} The given arr after being reversed.
 */
function reverseArr(items) {
    if(items.length <= 1) {
        return items;
    }
    for (let i = 0; i < items.length/2; i++) {
        let offset = (items.length-1) - i; 
        [items[i], items[offset]] = [items[offset], items[i]];

        // [a, b] = [b, a]
        /*
        also valid:
        let temp = items[offset]
        items[offset] = items[i]
        items[i] = temp
         */
    }
    return items;
}

console.log('\nOriginal array:', arr1);
console.log('Reversed arr:', reverseArr(arr1));
console.log('Expected arr:', expected1a);

console.log('\nOriginal array:', arr2);
console.log('Reversed arr:', reverseArr(arr2));
console.log('Expected arr:', expected2a);

console.log('\nOriginal array:', arr3);
console.log('Reversed arr:', reverseArr(arr3));
console.log('Expected arr:', expected3a);

console.log('\nOriginal array:', arr4);
console.log('Reversed arr:', reverseArr(arr4));
console.log('Expected arr:', expected4a);

