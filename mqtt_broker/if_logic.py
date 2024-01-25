import sqlite3
from datetime import datetime, timedelta
import time

#Variables (DELETE IF CONNECTED TO DB)
datetime_from_payload = "2024-01-09T08:30:25.339113601+00:00"
date_from_booking="2024-01-09"
time_from_booking="08:32"
bluetooth_tag_from_payload="ZTW541"


# Connect to the SQLite database
conn = sqlite3.connect('smartparkingSDM.sqlite')
cursor = conn.cursor()

#Get user's id from bluetooth tag in the payload
cursor.execute('''SELECT user_id FROM User WHERE (bt_tag==?)''',(bluetooth_tag_from_payload,))
user_ID_from_payload_list = cursor.fetchall()
user_ID_from_payload=user_ID_from_payload_list[0][0]

#Get times that match to the user,date and parking Spot
#SOS ΕΧΩ ΒΑΛΕΙ ΝΑ ΕΛΕΓΧΕΙ OFFSTREETPARKING ΑΝΤΙ ΓΙΑ PARKING SPOT -> ΠΡΕΠΕΙ ΝΑ ΠΕΡΑΣΩ ΤΙΜΕΣ ΣΤΟ PARKING SPOT ΚΑΙ ΝΑ ΤΟ ΑΛΛΑΞΩ
cursor.execute('''SELECT time FROM Booking
WHERE (refUser==? and date="2024-01-09" and refOffStreetParking="ECE Area 1")''',(user_ID_from_payload,))
times_that_match_list=cursor.fetchall()
times_that_match = [item[0] for item in times_that_match_list]
print(times_that_match,type(times_that_match))
               
conn.close()

#Check if the right car parked (payload's bluetooth tag = booking's bluetooth tag)
parkedCar=True

# Check if the driver parked on time (payload's time = booking's time +- 10 mins)
date_from_payload = datetime_from_payload[:10]
time_from_payload = datetime_from_payload[11:16]
time_from_payload_formatted = datetime.strptime(time_from_payload, "%H:%M")
time_from_booking_formatted = datetime.strptime(time_from_booking, "%H:%M")
ten_minutes = timedelta(minutes=10)
if (date_from_payload==date_from_booking):
    if (time_from_payload_formatted - ten_minutes <= time_from_booking_formatted <= time_from_payload_formatted + ten_minutes):
        on_time=True
    else:
        on_time=False

#If logic
'''if (parkedCar==False):
    print("SomeoneParked but not the right person. The light stays OFF")
elif (parkedCar==True):
    print("The right driver parked. Let's check if they were on time.")
    if (on_time==True):
        print("The driver parked on time. The light is ON for 2 minutes")
        time.sleep(120)  # 2 minutes = 120 seconds
        print("2 minutes passed. The light is OFF")
    elif (on_time==False):
        print("The driver didn't park on time. The light stays OFF")'''

