import express from 'express'

const router = express.Router()

router.get('/', (req,res) => {
    res.redirect('/home')
});

router.get('/home', (req, res) => {
    try {
        res.render('home');
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

router.get('/home_faculty', (req, res) => {
    const faculty="ECE"
    try {
        console.log("my faculty is",faculty)
        res.render('home_faculty',{
            faculty: faculty})
        } 
        catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

router.get('/home_area', (req, res) => {
    const area="1"
    try {
        res.render('home_area',{
            area: area})
        } 
        catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

export default router