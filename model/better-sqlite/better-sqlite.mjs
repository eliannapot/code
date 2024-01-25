import sqlite from 'better-sqlite3';
const db = new sqlite('model/database/smartparkingSDM.sqlite');

export let getParkingSiteName = () => {
    const query = db.prepare('SELECT name FROM OffStreetParking');
    let info;
    try {
        info = query.all();
        return info;
    }
    catch (err) {
        throw err;
    }
}

export let newSiteDateTime = (user, parkingspot, selectedDate, reservation_code, selectedSite, selectedTime) => {
    const query = db.prepare('INSERT INTO Booking VALUES (?, ?, ?, ?, ?, ?)');
    try {
        query.run(user, parkingspot, selectedDate, reservation_code, selectedSite, selectedTime);
        // console.log("reservation code is: " + reservation_code)
        return true;
    }
    catch (err) {
        throw err;           
    }
}

export let getParkingInformation = (reservation_code) => {
    const query = db.prepare('SELECT * FROM Booking WHERE reservation_code=?;');
    let info;
    try {
        info = query.all(reservation_code);
        return info;
    }
    catch (err) {
        throw err;
    }
}