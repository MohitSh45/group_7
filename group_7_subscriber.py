# group_7_subscriber.py
import json
import paho.mqtt.client as mqtt
from group_7_util import print_data

BROKER = "test.mosquitto.org"
TOPIC = "group7/health"

def on_message(client, userdata, msg):
    try:
        
        decoded = msg.payload.decode("utf-8")
        data = json.loads(decoded)
        print_data(data)
        print(f"Received message: {decoded}")
        print(f"Message topic: {msg.topic}")
    except Exception as e:
        print(f"Error decoding message: {e}")

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)
print(f"Subscribed to topic: {TOPIC}")

client.loop_forever()
