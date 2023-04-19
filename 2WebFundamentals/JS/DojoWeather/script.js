function loadWeatherFor(key) {
    var city = document.querySelector(key);
    var id = city.id;
    var idStr = id.charAt(0).toUpperCase() + id.slice(1)
    alert(`Loading weather report for ${idStr}.`)
}
function dismissCookieBar() {
    var cookieBar = document.querySelector('#cookie-notice')
    cookieBar.remove();
}
function getFahrenheitFrom(celsius) {
    return Math.round((celsius * (9/5)) + 32);
}
function getCelsiusFrom(fahrenheit) {
    return Math.round((fahrenheit - 32) * (5/9));
}
function setElementTemp(e, isCelsius) {
    var current = e.innerText.slice(0,e.innerText.length-1);
    var symbol = '\u00B0';
    if(isCelsius) {
        e.innerText = getCelsiusFrom(current) + symbol;
    } else {
        e.innerText = getFahrenheitFrom(current) + symbol;
    }
}

function convertTemp(elem) {
    var selectedIndex = elem.selectedIndex;
    var isCelsius = (selectedIndex == 0);
    var highs = document.querySelectorAll("div.temperatures>.high");
    var lows = document.querySelectorAll("div.temperatures>.low");
    console.log(highs);

    highs.forEach(e => setElementTemp(e, isCelsius));
    lows.forEach(e => setElementTemp(e, isCelsius));
}

