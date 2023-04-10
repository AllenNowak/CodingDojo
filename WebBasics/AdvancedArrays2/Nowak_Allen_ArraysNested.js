// Nowak_Allen_ArraysNested.js

function getOptimalLocation(array) {
    // For the given customer location array, calculate the distances between each pair of coordinates vs all the others
    // Create an array (Joe's locations) at the midpoints of these distances
    let midpoints = getAllMidPoints(array);
    
    // These midpoints are the best location for Joe's truck between each pair of customers
    // For all of Joe's locations, calculate the distances to all customers
    getDistancesFromCustomers(midpoints, array);

    // This could also be done as two nested Reductions, but I think that'd make it harder to follow
    // The optimal is the one with the lowest total 
    let min = Number.MAX_SAFE_INTEGER
    let minKey = ''
    for(var row in midpoints) {
        let distances = midpoints[row]
        let totalDistance = distances.reduce((accum, curr) => {return accum + curr}, 0)
        // When there are ties, just return the 1st match
        if (totalDistance<min) {
            min = totalDistance;
            minKey = row
        }
    }

    // console.log('minKey', minKey, 'min distance', min);
    return '['+minKey+']'
}
function testSeveralArraysOfLocations() {
    const tests = [
        {case:0, optimum: '[3,-3]', customers: [[1,-1],[3,-1],[1,-3],[3,-3],[5,-3]] },
        {case:1, optimum: '[1,-3]', customers: [[1,-1],[3,-1],[1,-3],[3,-3],[1,-5]] },
        {case:2, optimum: '[2,-1]', customers: [[1,-1],[3,-1],[1,-3]] },
        {case:3, optimum: '[2,-1]', customers: [[1,-1],[3,-1]] },
        {case:4, optimum: '[1,-2]', customers: [[1,-1],[1,-3]] },
    ];
    for(var test of tests) {
        const actual = getOptimalLocation(test.customers);
        const expct  = test.optimum;

        const isSuccessful = (actual.localeCompare(expct) == 0)
        if(isSuccessful) {
            console.log('Passed Case #', test.case);
        } else {
            console.log( `Case ${test.case} - Actual:${actual} Expectation: ${expct}`)
        }
    }
}

function getDistanceBetween(pointA, pointB) {
    if(pointA[0] == pointB[0] && pointA[1] == pointB[1]) { 
        return 0; 
    }

    return Math.abs(pointB[0] - pointA[0]) + Math.abs(pointB[1] - pointA[1])
}
function getMidpoint(pointA, pointB) {
    if(pointA[0] == pointB[0] && pointA[1] == pointB[1]) { 
        return pointA; 
    }
    const xcoord = Math.round(pointB[0] - ((pointB[0] - pointA[0])/2));
    const ycoord = Math.round(pointB[1] - ((pointB[1] - pointA[1])/2));

    return [xcoord, ycoord]
}
function testMidpointCalcs() {
    console.log('Testing mid point calculations');
    const expectedMidpoints = [[1,-1],[1,-1],[1,1],[1,1],[5,-5],[5,-5]];
    testCases.forEach((element, index) => {
        const expected = expectedMidpoints[index];

        const midPt = getMidpoint(...element);

        const result = (midPt.toString().localeCompare(expected.toString()) == 0) ? 'passed' : 'failed'
        console.log(`Test #${index}`, result)
    });
}

// Given an array of customer locations, store the midpoints between every pair of customer locations
function getAllMidPoints(locations) {
    let possibilities = [];
    for(var row=0; row<locations.length; row++) {
        for (let col = 0; col < locations.length; col++) {
            if(row == col) { 
                continue; 
            }
            const midpoint = getMidpoint(locations[row], locations[col]);
            const midpointStr = midpoint.toString();
            if(!possibilities[midpointStr]) {
                possibilities[midpointStr] = []
            }
        }
    }

    return possibilities;
}
function getDistancesFromCustomers(midpoints, locations) {
    for(var index in midpoints) {
        // array equality is a pita, split the coordinate string and coerce to ints
        const pointA = index.split(',').map(Number)
        const distances = locations.map( pointB => getDistanceBetween(pointA, pointB));
        midpoints[index] = distances
    }

    return midpoints
}

const testCases = [
    [[0,0], [2,-2]],    
    [[2,-2], [0,0]],    
    [[0,2], [2,0]],     
    [[2,0], [0,2]],     
    [[0,0], [10,-10]],  
    [[0,-10], [10,0]]
];
function testDistanceCalcs() {
    const expectedDistances = [4,4,4,4,20,20];
    for(var i=0; i<testCases.length; i++) {
        const dist = getDistanceBetween(...testCases[i] )

        console.log(`Actual = ${dist}, expectation = ${expectedDistances[i]}`)
    }
}

function testOneArrayOfLocations() {
    const testCusts = [[1,-1],[3,-1],[1,-3],[3,-3],[5,-3]]
    let midpoints = getAllMidPoints(testCusts);
    getDistancesFromCustomers(midpoints, testCusts);
    let min = Number.MAX_SAFE_INTEGER
    let minKey = ''
    for(var row in midpoints) {
        let distances = midpoints[row]
        let totalDistance = distances.reduce((accum, curr) => { return accum + curr})
        if (totalDistance<min) {
            min = totalDistance;
            minKey = row
        }
    }

    // console.log('minKey', minKey, 'min distance', min);
    console.log(`[${minKey}] is the optimal location`)
}

// testMidpointCalcs()
// testDistanceCalcs()
// testOneArrayOfLocations();
testSeveralArraysOfLocations();