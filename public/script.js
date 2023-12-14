//create options for parking spots in parking site: ECE1
document.addEventListener("DOMContentLoaded", function () {
    // Check if the current page is "/home_site"
    if (window.location.pathname === "/home_site") {
        var select = document.getElementById("parkingSpot");

        // Add the default option
        var defaultOption = document.createElement("option");
        defaultOption.value = "";
        defaultOption.text = "Select a spot";
        defaultOption.disabled = true;
        defaultOption.selected = true;
        select.appendChild(defaultOption);

        // Generate options from Spot 1 to Spot 16
        for (var i = 1; i <= 16; i++) {
            var option = document.createElement("option");
            option.value = i;
            option.text = "Spot " + i;
            option.style.fontSize = "16px";
            select.appendChild(option);
        }
    }
});

//*************************************************************************** */

//redirect from /home to /home_site when clicking on the "Continue" button

function submitForm() {
    var form = document.getElementById('bookingForm');

    if (form.checkValidity()) {
        window.location.href = '/home_site';
    } else {
        alert("Please fill in all the required fields.");
    }
    
}



