const fs = require('fs');
const sqlite = require('better-sqlite3');

const createDatabase = () => {
  const databaseName = 'smartparkingSDM.sqlite';
  const db = new sqlite(databaseName);

  const sqlFile = 'database.sql';

  try {
    // Read SQL statements from the file
    const sqlStatements = fs.readFileSync(sqlFile, 'utf8');

    // Execute SQL statements to create the database
    db.exec(sqlStatements);

    console.log('Database created successfully.');
  } catch (error) {
    console.error('Error creating database:', error);
  } finally {
    // Close the database connection
    db.close();
  }
};

createDatabase();
