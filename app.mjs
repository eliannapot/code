import express from 'express';
import { engine } from 'express-handlebars';
import router from './routes/router.mjs';
import session from 'express-session';


const app = express();
const PORT = process.env.PORT || '3001';

app.use(express.static('public'));

app.engine('hbs', engine({ extname: 'hbs' }))
app.set('view engine', 'hbs');

app.use('/',router);

const server = app.listen(PORT, () => {
    console.log(`http://127.0.0.1:${PORT}`);
});
