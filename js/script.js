function displayDate() {
    const date  = new Date();
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
setInterval(displayDate,1000); //update in real time every 1 second

//Pin pad
document.getElementById("punch-in-btn").addEventListener("click", function() {
    document.getElementById("pin-pad-container").style.display = "block";
});

let pin = "";

function enterPin(number) {
    if (pin.length < 4) {
        pin += number;
        document.getElementById("pin-display").textContent = "*".repeat(pin.length);
    }
}

function clearPin() {
    pin = "";
    document.getElementById("pin-display").textContent = "Enter PIN";
}

function submitPin() {
    if (pin.length === 4) {
        alert("PIN Submitted: " + pin);
        // add logic here for what happens when the PIN is correct.
        clearPin();
        document.getElementById("pin-pad-container").style.display = "none";
    } else {
        alert("Please enter a 4-digit PIN");
    }
}

function exitPinPad() {
    clearPin();
    document.getElementById("pin-pad-container").style.display="none";
}
