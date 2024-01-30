import sqlite3

payload_dict={
    "deduplicationId": "8f1d61e8-18f5-43fa-a873-ed2372a24568",
    "time": "2023-12-06T08:30:25.339113601+00:00",
    "deviceInfo": {
        "tenantId": "063a0ecb-e8c2-4a13-975a-93d791e8d40c",
        "tenantName": "Smart Campus",
        "applicationId": "f3b95a1b-d510-4ff3-9d8c-455c59139e0b",
        "applicationName": "Parking",
        "deviceProfileId": "1f6e3708-6d76-4e0f-a5cb-30d27bc78158",
        "deviceProfileName": "Cicicom S-LG3T",
        "deviceName": "cicicom-s-lg3t:2",
        "devEui": "0004a30b00e95f14",
        "tags": {
            "manufacturer": "Cicicom",
            "deviceId": "cicicom-s-lg3t:1",
            "apiKey": "4jggokgpesnvfb2uv1s40d73ov",
            "model": "S_LG3T"
        }
    },
    "devAddr": "0133177d",
    "adr": True,
    "dr": 5,
    "fCnt": 599,
    "fPort": 1,
    "confirmed": True,
    "data": "NzMuMjcxAAAxgiszMy4w",
    "object": {
        "temperature": "+33.0",
        "batteryVoltage": "3.27",
        "tag": "",
        "carStatus": 1
    },
    "rxInfo": [
        {
            "gatewayId": "1dee1a0843acf826",
            "uplinkId": 58140,
            "rssi": -101,
            "snr": 8.8,
            "channel": 1,
            "rfChain": 1,
            "location": {
                "latitude": 38.288395556071336,
                "longitude": 21.788930292281066
            },
            "context": "9lxByw==",
            "metadata": {
                "region_common_name": "EU868",
                "region_config_id": "eu868"
            },
            "crcStatus": "CRC_OK"
        }
    ],
    "txInfo": {
        "frequency": 868300000,
        "modulation": {
            "lora": {
                "bandwidth": 125000,
                "spreadingFactor": 7,
                "codeRate": "CR_4_5"
            }
        }
    }
}

# Extract values from payload
device_ID = payload_dict.get('devEui')
bluetooth_tag = payload_dict.get('object', {}).get('tag')
dateLastValueReported = payload_dict.get('time')

#Standard Values
TYPE="Device"
controlledProperty="movementActivity"
deviceCategory="sensor"

# Connect to the SQLite database
conn = sqlite3.connect('smartparkingSDM.sqlite')
cursor = conn.cursor()

# Insert the values into the Device table

# cursor.execute('''
#     INSERT INTO Device (id, value, dateLastValueReported, type, controlledProperty, deviceCategory)
#     VALUES (?, ?, ?, ?, ?, ?)
# ''', (device_ID, bluetooth_tag, dateLastValueReported, TYPE, controlledProperty, deviceCategory))

#Update ParkingSpot's status to occupied
cursor.execute("UPDATE ParkingSpot SET status='occupied' WHERE refDevice=?",(device_ID,))

conn.commit()
conn.close()
