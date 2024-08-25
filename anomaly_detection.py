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
