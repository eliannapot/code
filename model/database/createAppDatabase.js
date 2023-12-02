const sqlite = require('better-sqlite3');

const createDatabase = () => {

  const databaseName = 'smartparking.sqlite'; //name
  const db = new sqlite(databaseName); //create empty sqlite file

  const sqlFile = 'database.sql'; //get the info
  const sqlStatements = require('fs').readFileSync(sqlFile, 'utf8'); //run it

  db.exec(sqlStatements); //create database

  console.log('Database created successfully.');

  db.close();
};

createDatabase();