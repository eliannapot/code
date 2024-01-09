import express from 'express'

const homeController = await import(`../controller/home.mjs`)

const router = express.Router()

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

router.get('/home_site', (req, res) => {
    const site="ECE_1"
    try {
        res.render('home_site',{
            site: site})
        } 
        catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

//for POST requests
router.use(express.urlencoded({extended: true}));

router.post('/home/submit-form', homeController.saveSiteDateTime);

// happens in controller actually
// router.post('/home/submit-form', async(req, res) => {
//     res.redirect('/home_site')
// });

export default router