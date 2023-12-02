const sqlite = require('better-sqlite3');
const db = new sqlite('../database/smartparking.sqlite');

//insert test from db to front
// 'use strict';

// import db from 'better-sqlite3'
// const sql = new db('model/database/gymspot.sqlite', { fileMustExist: true });
// // Τι χρειαζομαι το const sql = new db....

// export let readUser = (user) => {
//     const stmt = sql.prepare('SELECT * FROM User task WHERE username = ?');
//     let info;
//     try {
//         info = stmt.all(user.username);
//         return true;
//     }
//     catch (err) {
//         throw err;
//     }
// }

//test from front to db (?)
// 'use strict';

// import db from 'better-sqlite3'
// const sql = db('../database/gymspot.sqlite');
// // Τι χρειαζομαι το const sql = new db....

// export let addUser = (user) => {
//     const stmt = sql.prepare('INSERT INTO User VALUES (?, ?, ?, 0)');
//     let info;

//     try {
//         info = stmt.run(user.username, user.email, user.password);
//         return true;
//     }
//     catch (err) {
//         throw err;
//     }
// }