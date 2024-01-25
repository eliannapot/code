from paho.mqtt import client as mqtt_client
import time

def connect_mqtt(): 
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            publish(client)
        else:
            print("Failed to connect, return code %d\n", rc)
    
    broker = 'broker.emqx.io'
    port = 1883
    # username = 'emqx'
    # password = 'public'

   
    client_id = "elianna"
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    # print(type(client))
    return client


def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 10:
            break
        
def run():  
    client = connect_mqtt()
    client.loop_forever()


if __name__ == '__main__':
    
    #topic = "#"
    topic = "python/mqtt"
     
    run()
