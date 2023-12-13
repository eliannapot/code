CREATE TABLE User (
    user_id INTEGER PRIMARY KEY,
    user_pwd CHAR,
    bt_tag CHAR
);

CREATE TABLE OffStreetParking (
    id VARCHAR PRIMARY KEY,
    type STRING DEFAULT 'OffStreetParking',
    location VARCHAR,
    name STRING,
    images VARCHAR
);

CREATE TABLE ParkingSpot (
    id VARCHAR PRIMARY KEY,
    name STRING,
    type STRING DEFAULT 'ParkingSpot',
    status STRING,
    category STRING DEFAULT 'offStreet',
    location VARCHAR,
    refParkingSite VARCHAR,
    refDevice VARCHAR
);

CREATE TABLE Device (
    id VARCHAR PRIMARY KEY,
    type STRING DEFAULT 'Device',
    ControlledProperty VARCHAR DEFAULT 'movementActivity',
    deviceCategory VARCHAR DEFAULT 'Sensor',
    value VARCHAR DEFAULT NULL,
    dateLastValueReported DATETIME
);

CREATE TABLE Streetlight (
    id INTEGER PRIMARY KEY,
    location VARCHAR,
    status STRING,
    type STRING DEFAULT 'streetLight',
    powerState STRING,
    dateLastSwitchingOn DATETIME,
    refDevice VARCHAR
);

CREATE TABLE Booking (
    refUser INTEGER REFERENCES User(user_id),
    refParkingSpot VARCHAR REFERENCES ParkingSpot(id),
    datetime DATETIME,
    reservation_code INTEGER PRIMARY KEY
);
