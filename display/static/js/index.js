// document.addEventListener("DOMContentLoaded", function () {
//     const pingResultsDiv = document.getElementById("pingResults");

//     // Function to fetch and display ping results
//     function displayPingResults() {
//         fetch("/ping_results.json") // Change the URL to the location of your JSON file
//             .then(response => response.json())
//             .then(data => {
//                 pingResultsDiv.innerHTML = ""; // Clear previous results

//                 for (const ip in data) {
//                     const result = data[ip];
//                     const resultElement = document.createElement("div");
//                     resultElement.textContent = `${ip}: ${result}`;
//                     pingResultsDiv.appendChild(resultElement);
//                 }
//             })
//             .catch(error => {
//                 console.error("Error fetching ping results:", error);
//             });
//     }

//     // Call the displayPingResults function to load and display ping results
//     displayPingResults();
// });
// script.js
function readLocalCSVFile() {
    fetch('data.csv') // Relative path to your CSV file
        .then(response => response.text())
        .then(csvdata => {
            // Split by line break to get rows Array
            var rowData = csvdata.split('\n');

            // <table> <tbody>
            var tbodyEl = document.getElementById('tblcsvdata').getElementsByTagName('tbody')[0];
            tbodyEl.innerHTML = "";

            // Loop on the row Array (change row=0 if you also want to read 1st row)
            for (var row = 1; row < rowData.length; row++) {

                // Insert a row at the end of the table
                var newRow = tbodyEl.insertRow();

                // Split by comma (,) to get column Array
                rowColData = rowData[row].split(',');

                // Loop on the row column Array
                for (var col = 0; col < rowColData.length; col++) {

                    // Insert a cell at the end of the row
                    var newCell = newRow.insertCell();
                    newCell.innerHTML = rowColData[col];

                }
            }
        })
        .catch(error => {
            console.error("Error reading local CSV file:", error);
        });
}

// Call the readLocalCSVFile function
readLocalCSVFile();
