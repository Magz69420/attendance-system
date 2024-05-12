document.getElementById("download-btn").addEventListener("click", function() 
{
    // Get the selected date
    var selectedDate = document.getElementById("selected_date").value;

    // Create a new AJAX request
    var xhr = new XMLHttpRequest();

    // Set up the request
    xhr.open("POST", "/download", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // Set up the callback
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Create a blob object from the response
            var blob = new Blob([xhr.response], { type: 'text/csv' });

            // Create a temporary link element
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = "attendance_data.csv";

            // Simulate clicking the link to trigger the download
            document.body.appendChild(link);
            link.click();

            // Clean up
            document.body.removeChild(link);
        } else {
            console.error('Error downloading data: ' + xhr.statusText);
        }
    };

    // Send the request with selectedDate as JSON
    xhr.send(JSON.stringify({ selected_date: selectedDate }));
});
