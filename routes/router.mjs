import express from 'express'
import session from 'express-session';

const homeController = await import(`../controller/home.mjs`)

const router = express.Router()

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

router.get('/', (req, res) => {
    res.redirect('/home')
});

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

router.post('/home/submit-form',  async (req,res) => {
    const reservation_code = generateRandomInteger(); 
    req.session.reservation_code = reservation_code;
    try {
        homeController.saveSiteDateTime(reservation_code, req, res);

    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }});

router.get('/home_site', async (req,res) => {
    const site="ECE_1" 
    try {
        const site = await homeController.showParkingSite(req.session.reservation_code);

        console.log("site: ", site);
        console.log("image: ", req.body)

        res.render('home_site',{
            site: site[0].refOffStreetParking })
        } 
        catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});


export default router