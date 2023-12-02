-- User table
CREATE TABLE User (
    user_id INTEGER PRIMARY KEY,
    user_pwd CHAR,
    bt_tag CHAR
);

-- Booking table
CREATE TABLE Booking (
    user_id INTEGER,
    parking_id INTEGER,
    date FLOAT,
    time FLOAT,
    reservation_code INTEGER PRIMARY KEY,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (parking_id) REFERENCES Parking_Spot(parking_id)
);

-- Parking_Sensor table
CREATE TABLE Parking_Sensor (
    ps_id INTEGER PRIMARY KEY,
    ps_status BOOLEAN
);

-- Lighting_Controller table
CREATE TABLE Lighting_Controller (
    lc_id INTEGER PRIMARY KEY,
    lc_status BOOLEAN
);

-- Parking_Spot table
CREATE TABLE Parking_Spot (
    parking_id INTEGER PRIMARY KEY,
    faculty CHAR,
    area INTEGER,
    spot INTEGER
);

-- Activates table
CREATE TABLE Activates (
    ps_id INTEGER,
    lc_id INTEGER,
    date FLOAT,
    time FLOAT,
    PRIMARY KEY (ps_id, lc_id),
    FOREIGN KEY (ps_id) REFERENCES Parking_Sensor(ps_id),
    FOREIGN KEY (lc_id) REFERENCES Lighting_Controller(lc_id)
);

-- Has table
CREATE TABLE Has (
    parking_id INTEGER,
    ps_id INTEGER,
    PRIMARY KEY (parking_id, ps_id),
    FOREIGN KEY (parking_id) REFERENCES Parking_Spot(parking_id),
    FOREIGN KEY (ps_id) REFERENCES Parking_Sensor(ps_id)
);
