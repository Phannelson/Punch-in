console.log("JavaScript file loaded successfully");

// Display current date and time
function displayDate() {
    const date = new Date();
    const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        hour12: 'true'
    };
    const formattedDate = date.toLocaleDateString('en-US', options);
    document.getElementById("current-date").textContent = formattedDate;
}

displayDate();
setInterval(displayDate, 1000); // Update every second

// Pin pad functions
document.getElementById("punch-in-btn").addEventListener("click", function() {
    console.log("Punch In button clicked");
    document.getElementById("pin-pad-container").style.display = "block";
});

let pin = "";

function enterPin(number) {
    console.log("Entered number:", number);
    if (pin.length < 4) {
        pin += number;
        console.log("Current PIN:", pin);
        document.getElementById("pin-display").textContent = "*".repeat(pin.length);
    }
}

function clearPin() {
    console.log("Clear PIN function called");
    pin = "";
    document.getElementById("pin-display").textContent = "Enter PIN";
}

function exitPinPad() {
    console.log("Exit Pin Pad function called");
    clearPin();
    document.getElementById("pin-pad-container").style.display = "none";
}

function submitPin() {
    console.log("Submit PIN function called");
    console.log("Entered PIN:", pin);

    if (pin.length === 4) {
        // Send the PIN to the server using fetch
        console.log("Sending PIN to server...");
        fetch('/punch-in/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken() // Ensure CSRF token is provided for security
            },
            body: JSON.stringify({
                pin: pin,
                time: new Date().toISOString() // Send current time as well
            })
        })
        .then(response => {
            console.log("Fetch response received");
            return response.json();
        })
        .then(data => {
            console.log("Server response:", data); // Log the response for debugging
            if (data.success) {
                document.getElementById('response-message').textContent = 'Punch-in successful!';
            } else {
                document.getElementById('response-message').textContent = 'Invalid PIN. Please try again.';
            }
            clearPin();
            document.getElementById("pin-pad-container").style.display = "none";
        })
        .catch(error => {
            console.error('Error during fetch:', error); // Log any errors for debugging
            document.getElementById('response-message').textContent = 'Error connecting to server.';
        });
    } else {
        console.log("Invalid PIN length. Must be 4 digits.");
        alert("Please enter a 4-digit PIN");
    }
}

// CSRF Token Helper Function
function getCSRFToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
            return decodeURIComponent(cookie.substring(name.length + 1));
        }
    }
    return null;
}
