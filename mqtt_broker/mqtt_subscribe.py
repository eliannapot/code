import json #useful for making message payload to type dictionary (json file)

from paho.mqtt import client as mqtt_client

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
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    # print(type(client))
    return client

def subscribe(client):
    
    def on_message(client, userdata, msg):
       
        # Decode bytes to string
        payload_str = msg.payload.decode('utf-8')
        try:
            payload_str = payload_str.replace("'", '"')
            # Parse JSON data
            payload_dict = json.loads(payload_str)
            #print("payload_dict=",payload_dict)
            if 'deviceName' in payload_dict and payload_dict['deviceName'] == "cicicom-s-lg3t:2":
                print("Filtered payload:", payload_dict)
        except json.decoder.JSONDecodeError:
            #print("json.decoder.JSONDecodeError")
            pass

    client.subscribe(topic)
    client.on_message = on_message

def run():  
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    
    topic = "#"
    
    run()
