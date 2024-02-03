import json 

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
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client):
    #processed_messages = set()  # Set to store processed messages

    def on_message(client, userdata, msg):
        '''device_name_in_bytes = b'cicicom-s-lg3t:2'
        print(msg.payload)
        if device_name_in_bytes in msg.payload:
            print("raw payload:", msg.payload)
            # Decode bytes to string
            payload_str = msg.payload.decode('utf-8')
            payload_str = payload_str.replace("'", '"')
            try:
                # Parse JSON data
                payload_dict = json.loads(payload_str)
                # Check if deduplicationId is in the set of processed messages
                if payload_dict.get('deduplicationId') not in processed_messages:
                    processed_messages.add(payload_dict.get('deduplicationId'))
                    print("Filtered payload:", payload_dict)
            except json.decoder.JSONDecodeError:
                print("json.decoder.JSONDecodeError")
                pass'''
        
        print("filtered payload=", msg.payload)
            # Decode bytes to string
        payload_str = msg.payload.decode('utf-8')
        payload_str = payload_str.replace("'", '"')
        try:
            # Parse JSON data
            payload_dict = json.loads(payload_str)
            print("json payload:", payload_dict)
        except json.decoder.JSONDecodeError:
            print("json.decoder.JSONDecodeError")
            pass

    client.subscribe(topic)
    client.on_message = on_message


def run():  
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    
    topic = "json/Parking/cicicom-s-lg3t:2"
    #topic = "json/Parking/#"
    #topic = #
    
    run()
