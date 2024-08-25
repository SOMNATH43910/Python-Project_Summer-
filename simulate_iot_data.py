import paho.mqtt.client as mqtt
import time
import random

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "health/data"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message published: {mid}")

def simulate_health_data():
    client = mqtt.Client("HealthSimulator")
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.connect(BROKER, PORT, 60)
    client.loop_start()

    try:
        while True:
            heart_rate = random.randint(60, 100)
            temperature = round(random.uniform(36.0, 38.5), 1)
            oxygen_level = round(random.uniform(95.0, 100.0), 1)

            message = f"Heart Rate: {heart_rate}, Temperature: {temperature}, Oxygen Level: {oxygen_level}"
            client.publish(TOPIC, message)

            time.sleep(5)  # Publish every 5 seconds

    except KeyboardInterrupt:
        print("Simulation interrupted by user.")
    finally:
        client.loop_stop()
        client.disconnect()
        print("Disconnected from broker.")

if __name__ == "__main__":
    simulate_health_data()
