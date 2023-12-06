import express from 'express'

const router = express.Router()

router.get('/', (req, res) => {
    res.redirect('/home')
});

router.get('/home', async (req,res) => {
    console.log('This should always log');
    try{
        const site="ECE_1"
        console.log("my site is",site);
        res.render('home',{
            site: site
        });
    }
    catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

//ΠΡΟΒΛΗΜΑ: 
//*ΌΤΑΝ ΕΙΜΑΙ ΣΤΟ "/": ΕΝΩ ΚΑΝΕΙ RENDER ΣΤΟ HOME.HBS ΔΕΝ ΚΑΝΕΙ ΚΑΝΕΝΑ CONSOLE LOG ΑΡΑ ΔΕΝ ΔΟΥΛΕΥΕΙ Ο ΚΩΔΙΚΑΣ ΤΟΥ /HOME
//*ΌΤΑΝ ΕΙΜΑΙ ΣΤΟ "/HOME":ΔΟΥΛΕΥΕΙ ΤΕΛΕΙΑ ΑΛΛΑ ΠΡΕΠΕΙ ΝΑ ΤΟ ΠΑΤΑΩ ΧΕΙΡΟΚΙΝΗΤΑ
//* ΑΝ ΚΡΑΤΗΣΩ ΜΟΝΟ ΤΟ "/" ΚΑΙ ΒΑΛΩ ΕΚΕΙ ΤΙΣ ΕΝΤΟΛΕΣ, ΕΚΤΕΛΕΙ ΤΟ RENDER ΑΛΛΑ ΟΧΙ ΤΑ CONSOLE LOG!
//VS CODE ΓΑΜΙΕΣΑΙ

// router.get('/home_faculty', (req, res) => {
//     const faculty="ECE"
//     console.log("my faculty is",faculty)
//     res.render('home_faculty',{
//         faculty: faculty})
// });

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

export default router