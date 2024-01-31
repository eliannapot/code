from paho.mqtt import client as mqtt_client
import time

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

   
def publish(client):
    msg = f"streetlightInfo: {{'powerState':'on'}}"
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
        
def run():  
    client = connect_mqtt()
    #client.loop_forever()
    publish(client)

if __name__ == '__main__':
    
    topic = "json/Parking/inteliLIGHT-FRE-220-NEMA-L"
     
    run()
