// Create a context menu for right-clicking
chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
        id: "verify-tweet", 
        title: "Verify",
        contexts: ["selection"]
    });
});

// Listen for menu item clicks
chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "verify-tweet") {
        // Run a script to handle the user's action
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            func: verifySelectedTweet,
            args: [info.selectionText]
        });
    }
});

// Function to verify the tweet
function verifySelectedTweet(tweet) {
    if (!tweet) {
        alert("No tweet text selected!");
        return;
    }

    // Define the API endpoint
    const apiUrl = "https://fake-tweet-detector-e8bc3d290749.herokuapp.com/classify";

    // Send the tweet to the API
    fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ tweet: tweet })
    })
    .then(response => response.json())
    .then(data => {
        const result = data.prediction || "unknown";
        alert(`The tweet is classified as: ${result}`);
    })
    .catch(error => {
        console.error("Error verifying tweet:", error);
        alert("Failed to verify the tweet. Please try again.");
    });
}