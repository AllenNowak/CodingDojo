function likeUniqueUsers(userId) {
    // This is a stand-in function
    // I expect that we'd never just take the argument without scrubbing potentially hazardous inputs
    likeSomething('#' + userId)
}

function likeSomething(idString) {
    var currentCountElement = document.querySelector(idString);
    let count = parseInt(currentCountElement.innerText);
    count++;

    currentCountElement.innerText = `${count}`;
}