const model = await import(`../model/better-sqlite/better-sqlite.mjs`)

//Generate reservation_code randomly
function generateRandomInteger() {
    const randomInteger = Math.floor(Math.random() * 90000000) + 10000000;
    return randomInteger;
}
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

export async function saveSiteDateTime(req,res) {
    
    const selectedSite = req.body.selectedSite;
    const selectedDate = req.body.selectedDate;
    const selectedTime = req.body.selectedTime;
    const reservation_code = generateRandomInteger();
    const user = defaultUser;
    const parkingspot = null

    console.log("area: ", selectedSite, typeof selectedSite);

    await model.newSiteDateTime(user, parkingspot, selectedDate, reservation_code, selectedSite, selectedTime);

    res.redirect('/home_site')
}