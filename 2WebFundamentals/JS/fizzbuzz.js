function fizzbuzz() {
    for(let i=1; i<=100; i++) {
        var fizzyString = ''
        if (i % 3 === 0) {
            fizzyString += 'Fizz'
        }
        if (i % 5 === 0) {
            fizzyString += 'Buzz'
        }
        var str = (fizzyString.length === 0) ? i : fizzyString
        console.log(str)
    }
}

fizzbuzz()
