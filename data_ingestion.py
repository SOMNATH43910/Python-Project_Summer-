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
