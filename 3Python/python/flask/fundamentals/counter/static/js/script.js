function toggleLogin(elem) {
    elem.innerText = "Logout";
}

function hide(elem) {
    elem.remove();
}

function update_submit(elem) {
    let curr_val = elem.value
    console.log('slider value', curr_val)

    let slider_value = document.getElementById("jumper")
    let button = document.querySelector("#subm")
    button.value = "Plus " + curr_val
    console.log(button.value)
    console.log(button)
}
