function sendMessage() {
    const msg = document.getElementById("messageInput").value;

    fetch("/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        alert("Server says: " + data.message);
    });
}
