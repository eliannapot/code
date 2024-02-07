from datetime import datetime, timedelta, timezone
from paho.mqtt import client as mqtt_client
import sqlite3
import time
import os
import json
import requests

def connect_to_db():
    script_dir = os.path.dirname(__file__)
    database_path = os.path.join(script_dir, '..', 'model', 'database', 'smartparkingSDM.sqlite')
    connection = sqlite3.connect(database_path)
    return connection

def check_the_booking(client, payload_dict):

    def save_payload_to_db():
        print("New Message from Sensor:",device_ID)
        print()
        #Update Device table
        cursor.execute("UPDATE Device SET (dateLastValueReported,value)=(?,?) WHERE id=?",(datetime_from_payload,bluetooth_tag,device_ID,))    
        conn.commit()

    def get_parkingspot_id():
        cursor.execute("SELECT id FROM ParkingSpot WHERE refDevice=?",(device_ID,))
        parking_spot_list=cursor.fetchall()
        if (parking_spot_list==[]):
            print("This Device does not refer to any Parking Spot")
            print()
        else:
            parking_spot=parking_spot_list[0][0]
        return parking_spot
    
    def check_if_car_parked():
        carStatus=payload_dict.get('object', {}).get('carStatus')
        if (carStatus==1):
            print("A car parked in the parking spot with ID: "+parking_spot)
            print()
            #Update ParkingSpot's status to occupied
            cursor.execute("UPDATE ParkingSpot SET status='occupied' WHERE refDevice=?",(device_ID,))
            conn.commit()
        elif (carStatus==0):
            print("There is no car parked in the parking spot with ID: "+parking_spot)
            print()
            #Update ParkingSpot's status to free
            cursor.execute("UPDATE ParkingSpot SET status='free' WHERE refDevice=?",(device_ID,))
            conn.commit()
        else:
            print("There has been an error in loading the car status")
            print()
        return carStatus

    def check_if_parking_valid():
        on_time=False
        #Get times that match to the user,date and parking spot
        cursor.execute("SELECT time FROM Booking WHERE (refUser==? and date=? and refParkingSpot=?)",(user_ID,date_from_payload,parking_spot))
        times_that_match_list=cursor.fetchall()
        if (times_that_match_list!=[]):
            times_that_match = [item[0] for item in times_that_match_list]
            # Check if the driver parked on time (payload's time = booking's time +- 10 mins)
            time_from_payload_formatted = datetime.strptime(time_from_payload, "%H:%M")
            ten_minutes = timedelta(minutes=10)
            for time_that_match in times_that_match:
                time_formatted = datetime.strptime(time_that_match, "%H:%M")
                if (time_from_payload_formatted - ten_minutes <= time_formatted <= time_from_payload_formatted + ten_minutes):
                    on_time=True    
                    break
                else:
                    on_time=False
        return on_time

    def get_user_id():
        user_id=""
        cursor.execute("SELECT user_id FROM User WHERE bt_tag==?",(bluetooth_tag,))
        user_ID_list = cursor.fetchall()
        if (user_ID_list!=[]):
            user_id=user_ID_list[0][0]
        return user_id

    def open_the_light():
        #Get Streetlight's ID
        cursor.execute("SELECT * FROM Streetlight WHERE refDevice==?",(device_ID,))
        streetlight_list=cursor.fetchall()
        if (streetlight_list==[]):
            print("This Device does not refer to any Streetlight.")
            print()
        else:
            streetlight_info=streetlight_list[0]
            #Set Streetlight's powerState to 'on'
            cursor.execute("UPDATE Streetlight SET powerState='on',dateLastSwitchingOn=? WHERE id=?",(datetime_from_payload,streetlight_info[0]),)
            conn.commit()
            #Publish To MQTT Broker
            publish(client,streetlight_info,'on',datetime_from_payload)
            #Patch Context Broker
            patch('on',datetime_from_payload)
            time.sleep(300)  # 5 minutes = 300 seconds
            print("5 minutes passed. The light is OFF")
            print()
            #Set Streetlight's powerState to 'off'
            cursor.execute("UPDATE Streetlight SET powerState='off' WHERE id=?",(streetlight_info[0],))
            conn.commit()
            publish(client,streetlight_info,'off',datetime_from_payload)
            patch('off',datetime_from_payload)


   
    #get variables from payload
    bluetooth_tag=payload_dict.get('object', {}).get('tag')
    device_ID= payload_dict["deviceInfo"]["devEui"]
    datetime_from_payload = payload_dict['time']
    date_from_payload = datetime_from_payload[:10]
    time_from_payload = datetime_from_payload[11:16]

    conn=connect_to_db()
    cursor = conn.cursor()
    try:
        save_payload_to_db()
        parking_spot=get_parkingspot_id()
        if (parking_spot):
            carStatus = check_if_car_parked()
            if (carStatus):
                user_ID=get_user_id()
                if(user_ID):
                    on_time=check_if_parking_valid()
                    if (on_time):
                        print("The car matches the one from the booking. The light is ON for 5 minutes")
                        print()
                        open_the_light()
            if (not(user_ID) or not(on_time)):
                print("There's no parking match based on the app. The light stays OFF")
                print()
    except sqlite3.OperationalError:
        print("Database not found")
        print()
    conn.close()


            
def generate_fake_data():
    
    payload_dict={
        "deduplicationId": "8f1d61e8-18f5-43fa-a873-ed2372a24568",
        "time": "2024-01-25T18:22:25.339113601+00:00",
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
            "tag": "SVL283",
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
    
    return payload_dict


def connect_mqtt(): 
    def on_connect(client, userdata, flags,rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    
    broker = '150.140.186.118'
    port = 1883
    client_id = "elianna"
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client):
    
    payload_dict = None
    
    def on_message(client, userdata, msg):
        nonlocal payload_dict
        #print("raw payload=", msg.payload)
        # Decode bytes to string
        payload_str = msg.payload.decode('utf-8')
        payload_str = payload_str.replace("'", '"')
        try:
            # Parse JSON data
            payload_dict = json.loads(payload_str)
            #print("Filtered payload:", payload_dict)
        except json.decoder.JSONDecodeError:
            print("json.decoder.JSONDecodeError")
            pass
        
    topic = "json/Parking/cicicom-s-lg3t:2"
    client.subscribe(topic)
    client.on_message = on_message
    
    while payload_dict is None:
        client.loop()  # Process incoming messages
        time.sleep(0.1)
    
    return payload_dict
    

def publish(client,streetlightInfo,powerState,dateLastSwitchingOn):
    topic = "json/Parking/inteliLIGHT-FRE-220-NEMA-L"
    msg = f"{{'id':'{streetlightInfo[0]}','location':{streetlightInfo[1]},'status':'{streetlightInfo[2]}', 'type':'{streetlightInfo[3]}','powerState':'{powerState}','dateLastSwitchingOn':'{dateLastSwitchingOn}','refDevice':'{streetlightInfo[6]}' }}"
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"[MQTT Broker] Send `{msg}` to topic `{topic}`")
        print()
    else:
        print(f"[MQTT Broker] Failed to send message to topic {topic}")
        print()

def patch(powerState,dateLastSwitchingOn):
    url="http://150.140.186.118:1026/v2/entities/Streetlight1.1/attrs"
    headers = {"Content-Type": "application/json"}
    payload = {
        "powerState": {
            "type": "Text",
            "value": powerState
        },
        "dateLastSwitchingOn": {
            "type": "DateTime",
            "value": dateLastSwitchingOn
        }
    }
    response = requests.patch(url, headers=headers, data=json.dumps(payload))
    if 200 <= response.status_code < 300:
        print("[Context Broker] Patched ",json.dumps(payload, indent=2)," to URL ",url)
        print()
    else:
        print("[Context Broker] Failed to patch ",json.dumps(payload, indent=2)," to URL ",url)
        print()
    
        
def run():  
    client = connect_mqtt()
   
    real_data=False #if True: reads data from MQTT Broker, else reads fake data

    if (real_data==True):
        payload=subscribe(client)
    else:
        payload=generate_fake_data()

    if (payload!=None):
        check_the_booking(client, payload)
    else:
        print("There has been an error loading payload")
    

if __name__ == '__main__':     
    run()



    
                

