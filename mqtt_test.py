import paho.mqtt.client as mqtt

# Define the callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(f"Message received: {msg.topic} {msg.payload}")

# Initialize the MQTT client
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect("broker.hivemq.com", 1883, 60)  # Example broker address

# Start the loop
client.loop_start()

# Publish a test message
client.publish("test/topic", "Hello, MQTT!")

