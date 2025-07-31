# group_7_publisher.py
import json
import time
import paho.mqtt.client as mqtt
from group_7_util import create_data

BROKER = "test.mosquitto.org"
TOPIC = "group7/health"

client = mqtt.Client()

client.connect(BROKER, 1883, 60)

try:
    for _ in range(5):  # Send 5 messages
        data = create_data()
        payload = json.dumps(data)
        client.publish(TOPIC, payload)
        print(f"Published: {payload}")
        time.sleep(2)  # Sleep for 2 seconds
finally:
    client.disconnect()
    print("Disconnected from broker.")
