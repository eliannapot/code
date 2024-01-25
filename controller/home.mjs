const model = await import(`../model/better-sqlite/better-sqlite.mjs`)


//Default User
let defaultUser = "dabbis6" ; 

export async function showParkingSiteName() {
    try {
        const parkingSiteName = await model.getParkingSiteName()
        return parkingSiteName
    } catch(err) {
        console.log(err);
//        res.send(err)
    }
}


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

export async function showParkingSite(reservation) {

    try {
        const parkingSiteInformation = await model.getParkingInformation(reservation)
        return parkingSiteInformation
    } catch(err) {
        console.log(err);
//        res.send(err)
    }
    console.log("home.mjs did sth")
}


export async function saveParkingSpot(reservation,req,res) {
    console.log("home.mjs saveParkingSpot " + req.body.selectedParkingSpot);
    await model.newSaveParkingSpot(req.body.selectedParkingSpot,reservation);
  
    res.redirect('/home')
}