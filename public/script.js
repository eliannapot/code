document.addEventListener("DOMContentLoaded", function () {
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
});



window.onload = function () {
    function submitForm() {
        var form = document.getElementById('bookingForm');

        if (form.checkValidity()) {
            // Check if the current page is /home before redirecting
            if (window.location.pathname === '/home') {
                window.location.href = "/home_faculty";
            } else {
                // Handle the case where the form should not be submitted on other pages
                alert("Form submission is allowed only on the /home page.");
            }
        } else {
            // The form is not valid, you can provide feedback to the user or take other actions
            alert("Please fill in all the required fields.");
        }
    }
};

