document.getElementById('send-btn').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== "") {
        addMessageToChatBox(userInput, 'user-message');
        document.getElementById('user-input').value = '';
        sendMessageToServer(userInput);
    }
});

function addMessageToChatBox(message, className) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${className}`;
    messageDiv.innerText = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}

function sendMessageToServer(message) {
    fetch('/get-llm-response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    })
    .then(response => response.json())
    .then(data => {
        addMessageToChatBox(data.response, 'bot-message');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}