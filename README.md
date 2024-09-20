//Main code

import data_ingestion
import simulate_iot_data  # Ensure this module is correctly implemented
import dashboard  # Ensure this module is correctly implemented

def main():
    print("=== Health Monitoring Dashboard ===2")
    print("1. Simulate Health Data")
    print("2. Start Data Ingestion")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        simulate_iot_data.simulate_health_data()
    elif choice == '2':
        dashboard.run_dashboard()
    elif choice == '3':
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()


    from sklearn.ensemble import IsolationForest
import numpy as np
from twilio.rest import Client

# Twilio credentials (Replace with actual credentials)
account_sid = 'AC0756b21ee3a7b51e73bf4c08070596e8'
auth_token = '9047795b90e6c0ea319e4c56940522f2'
twilio_phone_number = '+14343620856'
destination_phone_number = '+919749520371'

# Create Twilio client
twilio_client = Client(account_sid, auth_token)

def send_alert(message):
    try:
        twilio_client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=destination_phone_number
        )
        print("Alert sent successfully!")
    except Exception as e:
        print(f"Error sending alert: {e}")

# Train the model (dummy training data)
X_train = np.array([[70, 36.5, 98], [72, 36.7, 97], [75, 36.4, 99], [80, 36.8, 96]])
model = IsolationForest(contamination=0.1)
model.fit(X_train)

def detect_anomaly(new_data):
    pred = model.predict([new_data])
    if pred == -1:
        anomaly_message = f"Anomaly detected! Data: {new_data}"
        print(anomaly_message)
        send_alert(anomaly_message)
        return "Anomaly Detected"
    else:
        return "Normal"


        
import os

def run_dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    print("=== Health Monitoring Dashboard ===")
    print("1. Simulate Health Data")
    print("2. Start Data Ingestion")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            import simulate_iot_data
            simulate_iot_data.simulate_health_data()
        elif choice == '2':
            import data_ingestion
            data_ingestion.start_ingestion()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")





import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

BROKER = "broker.hivemq.com"
TOPIC = "health/data"

# Global variables for storing data
data = {'heart_rate': [], 'temperature': [], 'oxygen_level': []}

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, message):
    try:
        data_str = message.payload.decode("utf-8")
        parts = data_str.split(', ')
        heart_rate = float(parts[0].split(': ')[1])
        temperature = float(parts[1].split(': ')[1])
        oxygen_level = float(parts[2].split(': ')[1])

        # Append data to global lists
        data['heart_rate'].append(heart_rate)
        data['temperature'].append(temperature)
        data['oxygen_level'].append(oxygen_level)

        # Limit the length of data lists to keep the plot responsive
        max_length = 100
        if len(data['heart_rate']) > max_length:
            data['heart_rate'].pop(0)
            data['temperature'].pop(0)
            data['oxygen_level'].pop(0)

    except Exception as e:
        print(f"Error processing message: {e}")

def update_plot(frame):
    plt.clf()
    plt.subplot(3, 1, 1)
    plt.plot(data['heart_rate'], label='Heart Rate', color='blue')
    plt.legend(loc='upper right')
    plt.title("Heart Rate")

    plt.subplot(3, 1, 2)
    plt.plot(data['temperature'], label='Temperature', color='red')
    plt.legend(loc='upper right')
    plt.title("Temperature")

    plt.subplot(3, 1, 3)
    plt.plot(data['oxygen_level'], label='Oxygen Level', color='green')
    plt.legend(loc='upper right')
    plt.title("Oxygen Level")

def start_ingestion():
    client = mqtt.Client("DataIngestion")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER)
    client.loop_start()

    # Set up matplotlib for real-time plotting
    fig = plt.figure()
    ani = animation.FuncAnimation(fig, update_plot, interval=1000)
    plt.tight_layout()
    plt.show()

    try:
        while True:
            pass  # Keep the script running to process incoming messages

    except KeyboardInterrupt:
        print("Data ingestion interrupted by user.")
    finally:
        client.loop_stop()
        client.disconnect()
        print("Disconnected from broker.")

if __name__ == "__main__":
    start_ingestion()




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


    
