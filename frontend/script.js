function analyzeSentiment(type) {
    let textInput = type === 'title' ? document.getElementById('emailTitle').value : document.getElementById('emailContent').value;
    let apiUrl = 'http://localhost:8000/sentiment/'; // Replace with your FastAPI URL

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: textInput })
    })
    .then(response => response.json())
    .then(data => displayResults(data, type))
    .catch(error => console.error('Error:', error));
}

function displayResults(data, type) {
    let responseContainer = type === 'title' ? document.getElementById('titleResponseContainer') : document.getElementById('contentResponseContainer');
    responseContainer.innerHTML = `
        <h3>Results for ${type.charAt(0).toUpperCase() + type.slice(1)}:</h3>
        <p>Positive: ${data.positive}</p>
        <p>Neutral: ${data.neutral}</p>
        <p>Negative: ${data.negative}</p>
    `;
}

function analyzeSentiment(type) {
    let textInput = type === 'title' ? document.getElementById('emailTitle').value : document.getElementById('emailContent').value;
    let sentimentApiUrl = 'http://localhost:8000/sentiment/'; // Replace with your FastAPI URL
    let ratingApiUrl = 'http://localhost:8000/rating/'; // Replace with your FastAPI URL

    fetch(sentimentApiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: textInput })
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data, type);
        if (type === 'content') {
            // Fetch rating for content
            fetch(ratingApiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: textInput })
            })
            .then(response => response.json())
            .then(ratingData => displayRating(ratingData.rating))
            .catch(error => console.error('Error:', error));
        }
    })
    .catch(error => console.error('Error:', error));
}

function displayRating(rating) {
    let starsContainer = document.getElementById('contentResponseContainer').querySelector('.stars');
    starsContainer.innerHTML = ''; // Clear out the old stars

    for (let i = 1; i <= 5; i++) {
        let star = document.createElement('span');
        star.className = 'star';
        if (i <= rating) {
            star.classList.add('filled');
        } else if (i - 0.5 === rating) {
            star.classList.add('half-filled');
        }
        star.textContent = '★'; // Use ★ for filled and ☆ for empty if you want different characters
        starsContainer.appendChild(star);
    }
}

function submitQuestion() {
    let content = document.getElementById('emailContent').value;
    let question = document.getElementById('questionInput').value;
    let questionApiUrl = 'http://localhost:8000/question/'; // Replace with your FastAPI URL

    fetch(questionApiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: content, question: question })
    })
    .then(response => response.json())
    .then(data => displayQuestionAnswer(data))
    .catch(error => console.error('Error:', error));
}

function displayQuestionAnswer(data) {
    let questionResponseContainer = document.getElementById('questionResponseContainer');
    // Update with how you want to display the data, e.g.:
    questionResponseContainer.innerHTML = `
        <h3>Answer:</h3>
        <p>${data.answer}</p>
    `;
}