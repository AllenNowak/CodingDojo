var theDojo = [ [1, 0, 1, 1, 1, 0, 4, 0, 8, 0],
                [3, 1, 0, 7, 0, 0, 6, 0, 8, 8],
                [5, 0, 7, 0, 3, 6, 6, 6, 0, 0],
                [2, 3, 0, 9, 0, 0, 6, 0, 8, 0],
                [6, 0, 3, 3, 0, 2, 0, 3, 0, 4],
                [0, 0, 3, 3, 0, 0, 2, 2, 3, 0],
                [0, 0, 0, 0, 5, 0, 1, 2, 0, 6],
                [2, 2, 2, 2, 0, 7, 1, 1, 1, 0],
                [5, 2, 0, 2, 0, 0, 0, 1, 1, 2],
                [9, 2, 2, 2, 0, 7, 0, 1, 1, 0] ];
var emptyDojo= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ];
var dojoDiv = document.querySelector("#the-dojo");
    
// Creates (n) random numbers & seeds them in the 2d array
/*
 * @param {number} the number of ninjas hiding in the array
 * @param {Array<any>} arr 
 * @returns {Array<any>} arr Better to test return values than side effects
*/
function seedArrayWithNNinjas (n, arr) {
    let length = arr[0].length;     // assuming a regular, non-ragged 2d matrix
    let height = arr.length;
    let maxFlatIndex = length * height;
    const maxReTries = n+4;
    let collisions = 0
    for (let i = 0; i < n && collisions<maxReTries; i++) {
        const rndm = Math.floor(Math.random() * maxFlatIndex);
        const row = Math.floor(rndm / height);
        const col = rndm % length;

        if(arr[row][col] == 0) {
          arr[row][col] = 1;
        } else {
          collisions++;
          i--;    // Try again, up until a point
        }
    }
    return arr;
}

// Creates the rows of buttons for this game
function render(aDojo) {
  var result = "";
    for(var i in aDojo) {
      for(var j in aDojo[i]) {
        result += `<button class="tatami" onclick="howMany(${i}, ${j}, this)"></button>`;
    }
  }
  return result;
}
    
// TODO - Make this function tell us how many ninjas are hiding 
//        under the adjacent (all sides and corners) squares.
//        Use i and j as the indexes to check theDojo.
function howMany(i, j, element) {
  console.log({i, j});
  if( ninjaWasHiding(i, j, element)) {
    dojoDiv.innerHTML = `<button onclick="location.reload()">restart</button>`; 
    return;
  }

  let count = 0
  for(let row =i-1; row<=i+1; row++) {
      for(let col =j-1; col<=j+1; col++) {
          if(!( row == i && col == j)) {
              count += checkSquare(row, col);
          }
      }
  }

  element.innerText = '' + count;
  return count;
}

function ninjaWasHiding(i, j, element) {
  return currentDojo[i][j] > 0;
}

function checkSquare(i,j) {
    if(i<0 || i>=currentDojo.length) return 0;
    if(j<0 || j>=currentDojo[i].length) return 0;

    return currentDojo[i][j];
}

// BONUS CHALLENGES
// 1. draw the number onto the button instead of alerting it
/*
  element.innerText = '' + count;
 */
// 2. at the start randomly place 10 ninjas into theDojo with at most 1 on each spot
var sparseDojo = seedArrayWithNNinjas(10, emptyDojo);
// 3. if you click on a ninja you must restart the game 
//    dojoDiv.innerHTML = `<button onclick="location.reload()">restart</button>`;
/*
  if( ninjaWasHiding(i, j, element)) {
    dojoDiv.innerHTML = `<button onclick="location.reload()">restart</button>`; 
    return;
  }
 */    

// start the game
// message to greet a user of the game
var style="color:cyan;font-size:1.5rem;font-weight:bold;";
console.log("%c" + "IF YOU ARE A DOJO STUDENT...", style);
console.log("%c" + "GOOD LUCK THIS IS A CHALLENGE!", style);
// shows the dojo for debugging purposes
const currentDojo = sparseDojo;
console.log('Current Dojo is')
console.table(currentDojo)

// adds the rows of buttons into <div id="the-dojo"></div> 
dojoDiv.innerHTML = render(currentDojo);
