import sqlite3
from datetime import datetime, timedelta, timezone
import time
import os

#Variables taken from payload
datetime_from_payload = '2024-01-25T18:23:25.339113601+00:00'
date_from_payload = datetime_from_payload[:10]
time_from_payload = datetime_from_payload[11:16]
bluetooth_tag_from_payload="SVL283"
device_ID="0004a30b00e95f14"

# Connect to the SQLite database
script_dir = os.path.dirname(__file__)
database_path = os.path.join(script_dir, '..', 'model', 'database', 'smartparkingSDM.sqlite')
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

#Get user's id given the bluetooth tag 
cursor.execute("SELECT user_id FROM User WHERE bt_tag==?",(bluetooth_tag_from_payload,))
user_ID_list = cursor.fetchall()
if (user_ID_list==[]):
    print("User is not registered")
else:
    on_time=False
    user_ID=user_ID_list[0][0]
    #Get parking spot ID given device ID
    cursor.execute("SELECT id FROM ParkingSpot WHERE refDevice=?",(device_ID,))
    parking_spot_list=cursor.fetchall()
    if (parking_spot_list==[]):
        print("This Device does not refer to any Parking Spot")
    else:
        parking_spot=parking_spot_list[0][0]
        #Get times that match to the user,date and parking spot
        cursor.execute("SELECT time FROM Booking WHERE (refUser==? and date=? and refParkingSpot=?)",(user_ID,date_from_payload,parking_spot))
        times_that_match_list=cursor.fetchall()
        if (times_that_match_list==[]):
            print("Wrong Parking. The light stays OFF")
        else:
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
            if (on_time==True):
                print("The driver parked on time. The light is ON for 5 minutes")
                #Get Streetlight's ID
                cursor.execute("SELECT id FROM Streetlight WHERE refDevice==?",(device_ID,))
                streetlight_id_list=cursor.fetchall()
                if (streetlight_id_list==[]):
                    print("This Device does not refer to any Streetlight.")
                else:
                    streetlight_id=streetlight_id_list[0][0]
                    #Set Streetlight's powerState to 'on'
                    cursor.execute("UPDATE Streetlight SET powerState='on',dateLastSwitchingOn=? WHERE id=?",(datetime_from_payload,streetlight_id),)
                    conn.commit()
                    time.sleep(300)  # 5 minutes = 300 seconds
                    print("5 minutes passed. The light is OFF")
                    #Set Streetlight's powerState to 'off'
                    cursor.execute("UPDATE Streetlight SET powerState='off' WHERE id=?",(streetlight_id,))
                    conn.commit()
            else:
                print("The driver didn't park on time. The light stays OFF")
conn.close()


    
                

