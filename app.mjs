import express from 'express';
import { engine } from 'express-handlebars'

const app = express();
const PORT = process.env.PORT || '3000';

app.use(express.static('public'));

app.engine('hbs',engine({ extname: 'hbs' }))
app.set('view engine', 'hbs');

app.get('/', (req, res) => {
    try {
        res.render('layouts/main');
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});


const server = app.listen(PORT, () => {
    console.log(`http://127.0.0.1:${PORT}`);
});
