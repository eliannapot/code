import { listOfParkingSpots } from './routes/router.mjs';

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

        // Add the options
        console.log("listOfParkingSpots: ", listOfParkingSpots);
        for (var i = 0; i < listOfParkingSpots.length; i++) {
            var option = document.createElement("option");
            option.value = listOfParkingSpots[i];
            option.text = listOfParkingSpots[i];
            option.style.fontSize = "16px";
            select.appendChild(option);
        }
    }
});

