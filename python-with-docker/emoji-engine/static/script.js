window.onload = function() {
    init()
}

const init = () => {
    const form = document.querySelector('#start-form');
    form.addEventListener("submit", processStartForm);

    const recPhotoButton = document.querySelector('#recommend-photo');
    recPhotoButton.addEventListener("click", getRecommendedPhoto);
}

const processStartForm = (e) => {
    if (e.preventDefault) e.preventDefault();

    const word = document.querySelector('#word').value;
    const start = document.querySelector('#start').value;

    startsWithRequest(word, start, (result) => {
        const textBox = document.querySelector("#result");
        textBox.innerHTML = result['starts-with'] ? "True" : "False";
    });

    return false;
}

const getRecommendedPhoto = () => {
    fetch('/photo-hub', {
        method: 'GET',
    }).then(res => res.json())
      .then(data => displayRecommendedPhoto(data.photo));
}

const displayRecommendedPhoto = (recommendedPhotoURL) => {
    const imgEl = document.querySelector('#recommended-photo');
    imgEl.src = recommendedPhotoURL;
}



const startsWithRequest = (word, start, cb) => {
    const reqBody = {word, start};

    fetch('/starts-with', {
        method: 'POST',
        headers: new Headers({
            'Content-Type': 'application/json'
        }),
        body: JSON.stringify(reqBody)
    }).then(res => res.json())
      .then(data => cb(data));
}

