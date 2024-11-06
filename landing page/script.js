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