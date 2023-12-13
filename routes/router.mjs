import express from 'express'

const router = express.Router()

router.get('/', (req, res) => {
    res.redirect('/home')
});

router.get('/home', async (req,res) => {
    try{
        const site="ECE_1"
        res.render('home',{
            site: site
        });
    }
    catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

router.get('/home_site', (req, res) => {
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