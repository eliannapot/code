const model = await import(`../model/better-sqlite/better-sqlite.mjs`)


//Default User
let defaultUser = "Elianna" ; 


//To display the correct ECE Areas
export async function showParkingSiteName() {
    try {
        const parkingSiteName = await model.getParkingSiteName()
        return parkingSiteName
    } catch(err) {
        console.log(err);
//        res.send(err)
    }
}

//To save the selected date,time and site
export async function saveSiteDateTime(reservation,req,res) {
    
    const selectedSite = req.body.selectedSite;
    const selectedDate = req.body.selectedDate;
    const selectedTime = req.body.selectedTime;
    const reservation_code = reservation ;
    const user = defaultUser;
    const parkingspot = null

    await model.newSiteDateTime(user, parkingspot, selectedDate, reservation_code, selectedSite, selectedTime);

    // console.log("home.mjs reservation code is: " + reservation_code)
  
    res.redirect('/home_site')
}

//To display the parking site in the big map
export async function showParkingSite(reservation) {

    try {
        const parkingSiteInformation = await model.getParkingInformation(reservation)
        return parkingSiteInformation
    } catch(err) {
        console.log(err);
//        res.send(err)
    }
}

//To display the correct Parking Spots of the Area
export async function showParkingSpots(parkingArea) {
    try {
        const parkingSpots = await model.getParkingSpots(parkingArea)
        return parkingSpots 
    } catch(err) {
        console.log(err);
//        res.send(err)
    }
}

//To save the selected parking spot (completes booking)
export async function saveParkingSpot(reservation,req,res) {
    // console.log("home.mjs saveParkingSpot " + req.body.selectedParkingSpot);
    await model.newSaveParkingSpot(req.body.selectedParkingSpot,reservation);
  
    res.redirect('/reservation')
}

//To display the parking site in the big map
export async function showBookingDetails(reservation) {

    try {
        const bookingDetails = await model.getBookingDetails(reservation);
        console.log("home.mjs showBookingDetails: ", bookingDetails);
        return bookingDetails 
    } catch(err) {
        console.log(err);
//        res.send(err)
    }
}