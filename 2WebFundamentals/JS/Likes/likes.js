function likeUser(userId) {
    var currentCountElement = document.querySelector("#" + userId);
    let count = parseInt(currentCountElement.innerText);
    count++;
    console.log(`Count now ${count}`)
    currentCountElement.innerText = `${count}`;
}
