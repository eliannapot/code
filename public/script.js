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

// document.addEventListener("DOMContentLoaded", function () {
//     var button = document.getElementById('submitButton');
//     if (button) {
//         button.addEventListener('click', submitForm);
//     }
// });

function submitForm() {
    var form = document.getElementById('bookingForm');
    var select = document.getElementById('parkingSpot');
    console.log("Form Submited");
    // Check if the elements are present
    if (!form || !select) {
        return;
    }

    // Check if the parking spot is selected
    if (!select.value) {
        alert("Please select a parking spot.");
        return;
    }

    if (form.checkValidity()) {
        // Check if the current page is /home before redirecting
        if (window.location.pathname === '/home') {
            window.location.href = "/home_site";
        } else {
            // Handle the case where the form should not be submitted on other pages
            alert("Form submission is allowed only on the /home page.");
        }
    } else {
        // The form is not valid, you can provide feedback to the user or take other actions
        alert("Please fill in all the required fields.");
    }
}



