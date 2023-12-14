import json #useful for making message payload to type dictionary (json file)
import ast #useful for making message payload to type dictionary (json file)

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
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        #print(f"\nTOPIC: `{msg.topic}` \n")
        
        # Decode bytes to string
        payload_str = msg.payload.decode('utf-8')

        # Convert single quotes to double quotes using ast
        payload_str = ast.literal_eval(payload_str)
        print("payload_str=",payload_str)
        print("type of payload_str=",type(payload_str))
        print("")

        # Parse JSON data
        payload_dict = json.loads(json.dumps(payload_str))
        print("payload_dict=",payload_dict)
        print("type of payload_dict=",type(payload_dict))
        
    client.subscribe(topic)
    client.on_message = on_message

def run():  
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    
    topic = "#"
    
    run()
