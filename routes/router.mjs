import express from 'express'
import session from 'express-session';

const homeController = await import(`../controller/home.mjs`)

const router = express.Router()

let listOfParkingSpots = [];

// Use the express-session middleware
router.use(session({
    secret: 'secretkey',
    resave: false,
    saveUninitialized: true
  }));

//Generate reservation_code randomly
function generateRandomInteger() {
    const randomInteger = Math.floor(Math.random() * 90000000) + 10000000;
    return randomInteger;
}

//Default
router.get('/', (req, res) => {
    res.redirect('/home')
});

//Gets the parking site names in the home form
router.get('/home', async (req,res) => {
    const site="ECE_1"
    try{
        const parkingSiteNames = await homeController.showParkingSiteName();
        res.render('home',{
            parkingSiteNames: parkingSiteNames

//            site: parkingSiteNames[0].name
        });
    }
    catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});


//for POST requests
router.use(express.urlencoded({extended: true}));

//Saves site,date,time to db
router.post('/home/submit-form',  async (req,res) => {
    const reservation_code = generateRandomInteger(); 
    req.session.reservation_code = reservation_code;
    try {
        homeController.saveSiteDateTime(reservation_code, req, res);

    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});


router.get('/home_site', async (req,res) => {
    const site="ECE_1" 

    try {
        //shows parking area chosen in the header
        const site = await homeController.showParkingSite(req.session.reservation_code);
        //console.log("found the area: " + site[0].refOffStreetParking);
        const parkingArea = site[0].refOffStreetParking;
        
        // res.render('home_site',{
        //     site: site[0].refOffStreetParking })
        
        //shows parking spots in the dropdown menu
        const parkingSpotsAvl = await homeController.showParkingSpots(parkingArea);
        listOfParkingSpots = parkingSpotsAvl.map(parkingSite => parkingSite.id);

        
        // console.log("parkingSpotsAvl: ", parkingSpotsAvl);
        // console.log("listOfParkingSpots: ", listOfParkingSpots);
        
        res.render('home_site',{
            site: site[0].refOffStreetParking,
            parkingSpots: listOfParkingSpots
        });
        //console.log("listOfParkingSpots: ", listOfParkingSpots);
        //return listOfParkingSpots;
    } 
    catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }

    
    
});



router.post('/home/submit-success', async (req,res) => {
    console.log("post to home/submit-success")
    try {
        homeController.saveParkingSpot(req.session.reservation_code, req, res);
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }});


export default router ; 
export { listOfParkingSpots };
